from decouple import config
import base64, requests, logging, time
from .models import Submission, SubmissionMeta
from datetime import datetime
from django.utils import timezone
# from .utils import *

logger = logging.getLogger(__name__)

LEET_STATS_URL = config('LEET_STATS_URL')
BEARER_TOKEN = config('BEARER_TOKEN')
SUB_REPO_URL = config('SUB_REPO_URL')
SUB_META_URL = config('SUB_META_URL')
headers = {'Accept': 'application/vnd.github+json', 'Authorization' : f'token {BEARER_TOKEN}'}
subs_url = f'{SUB_REPO_URL}/contents/submissions'

def validateQaData(data):
    try:
        return base64.b64decode(data.json()['content'])
    except Exception as e:
        logger.error(f"Error Validating data: {str(e)}", exc_info=True)
        return e

def getQaDataFromFiles(file_dir, filename):
    data = requests.get(subs_url+'/'+file_dir+'/'+filename, headers=headers)
    if data.status_code != 200:
        filename = 'solution.js'
        data = requests.get(subs_url+'/'+file_dir+'/'+filename, headers=headers)
    if data.status_code != 200:
        logger.error(f"Error finding submission file in repo - not a .py or .js solution", exc_info=True)
    return data


# Repo Sub Retrieval
def addSubmissionsToDbOnMetaMatch(submissions:list):
    for q_a in submissions:
        for k, v in q_a.items():
            k = ''.join([char for char in k if char.isalpha() or char == '-'])
            title = ' '.join([word.capitalize() for word in k.split('-')]).strip()
            question = v[0].decode('utf-8')
            answer = v[1].decode('utf-8')
            submissions_to_update = Submission.objects.filter(title=title, needsUpdate=True)
            # Check if any submissions are found
            if submissions_to_update.exists():
                logger.info(f"Updating submission with title: {title}")
                submissions_to_update.update(question=question, answer=answer, needsUpdate=False)


def retrieveQandAsFromSubmission(submission_folder_urls: list) -> list:
    q_and_as = []
    for sub_files in submission_folder_urls:
        question_data = getQaDataFromFiles(sub_files, 'README.md')
        answer_data = getQaDataFromFiles(sub_files, 'solution.py')
        if question_data and answer_data:
            question = validateQaData(question_data)
            answer = validateQaData(answer_data)
            if answer and question:
                q_and_as.append({sub_files:[question, answer]})
    if q_and_as:
        addSubmissionsToDbOnMetaMatch(q_and_as)

def retrieveSubmissionsFromRepo(max_count=1000):
    count = 1
    r = requests.get(subs_url, headers=headers)
    submission_folder_urls = []
    for submission_folder in r.json():
        file_dir = submission_folder['name']
        submission_folder_urls.append(file_dir)
        count += 1
        if count > max_count:
            break
    if len(submission_folder_urls) > len(Submission.objects.all()):
        logger.info(f"Getting {len(submission_folder_urls) - len(Submission.objects.all())} more submission(s)")

    retrieveQandAsFromSubmission(submission_folder_urls)
    return ['Subs from Repo: ', len(submission_folder_urls)]


# META Retrieval
def createSubmissionFromMeta(submissions_list:list):
    logger.info( f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} : Attempting to create subs from meta")
    try:
        for sub in submissions_list:
            fetched_title = sub['title']
            fetched_date = sub['timestamp']
            formatted_fetch_date = timezone.make_aware(fetched_date)
            found_submission = Submission.objects.filter(title=fetched_title).first()
            if not found_submission: #Create if not found
                print(fetched_title, ' being created')
                Submission.objects.create(
                    title=fetched_title,
                    submitted_date=formatted_fetch_date
                )   
                logger.warning(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} Created {fetched_title}")

            else: #Update if Submission date newer
                if found_submission.submitted_date != formatted_fetch_date:
                    found_submission.submitted_date = formatted_fetch_date
                    found_submission.needsUpdate = True
                    found_submission.save()
    except Exception:
        logger.warning(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} Error in createSubmissionFromMeta {submissions_list}")

def filterSubmissionMeta(submissions:list):
    filtered_submissions = [sub for sub in submissions if sub['statusDisplay'] == 'Accepted']
    for submission in filtered_submissions:
        submission['timestamp'] = datetime.fromtimestamp(int(submission['timestamp']))
    print('3')

    createSubmissionFromMeta(filtered_submissions)

def retrieveSubmissionMetaFromLeetCode() -> list[dict]:
    leet_meta = requests.get(SUB_META_URL)
    if leet_meta.status_code == 200:
        data = leet_meta.json()
        if 'submission' in data:
            submissions = data['submission']     
            filterSubmissionMeta(submissions)
        else:
            logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}, No Meta submissions in { data } ", exc_info=True)
    else:
        logger.error(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} {leet_meta.status_code} response from Sub Meta URL", exc_info=True)



# Just stats on total solved
def retrieveLeetMetaStats():
    leetcode_summary = requests.get(LEET_STATS_URL)
    if leetcode_summary.status_code == 200:
        data = leetcode_summary.json() 
        prev_total = SubmissionMeta.objects.filter(pk=5).first().total_solved # access the one object holding my subStats
        if 'totalSolved' in data and data['totalSolved'] > prev_total: 
            try:
                obj, created = SubmissionMeta.objects.update_or_create(
                    pk = 5,
                    defaults={'total_solved': data['totalSolved'], 'easy_solved': data['easySolved'], 'medium_solved': data['mediumSolved'], 'hard_solved': data['hardSolved']},
                )
                return ['Total Solved: ', data['totalSolved']]

            except Exception as e:
                logger.error(f"Error updating leetcodeMeta: {e}")
        else:
            logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} No new solved questions {prev_total}")
            return 'Total Solved hasnt increased'
