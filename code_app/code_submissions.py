from decouple import config
import base64, requests, logging, time
from .models import Submission, SubmissionMeta
from datetime import datetime
from django.utils import timezone

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
            question = v[0]
            answer = v[1]
            submissions_to_update = Submission.objects.filter(title=title, needsUpdate=True)
            # Check if any submissions are found
            if submissions_to_update.exists():
                logger.info(f"Updating submission with title: {title}")
                submissions_to_update.update(question=question, answer=answer, needsUpdate=False)
            else: 
                logger.info(f"{title} doesnt need update")

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
    retrieveQandAsFromSubmission(submission_folder_urls)

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

# META Retrieval
def createSubmissionFromMeta(submissions:list):
    # print(submissions)
    for sub in submissions:
        new_title = sub['title']
        new_date = sub['timestamp']
        date_and_zone = timezone.make_aware(new_date)
        submission.submitted_date = date_and_zone

        try:
            submission = Submission.objects.get(title=new_title)
            if submission.submitted_date != new_date:
                submission.submitted_date = new_date
                submission.needsUpdate = True
                submission.save()
            else:
                # The data is identical; no need to update
                logger.info("No update needed, data is identical")
        except Submission.DoesNotExist:
            submission = Submission.objects.create(
                title=new_title,
                submitted_date=new_date
            )

def filterSubmissionMeta(submissions:list):
    filtered_submissions = [sub for sub in submissions if sub['statusDisplay'] == 'Accepted']
    for submission in filtered_submissions:
        submission['timestamp'] = datetime.fromtimestamp(int(submission['timestamp']))
    createSubmissionFromMeta(filtered_submissions)

def retrieveSubmissionMetaFromLeetCode() -> list[dict]:
        leet_meta = requests.get(SUB_META_URL)
        if leet_meta.status_code == 200:
                data = leet_meta.json()
                if 'submissions' in data:
                    submissions = data['submission']            
                    filterSubmissionMeta(submissions)
                else:
                    logger.error(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())} No Meta submissions in data ", exc_info=True)



def retrieveLeetMetaStats():
    leetcode_summary = requests.get(LEET_STATS_URL)
    if leetcode_summary.status_code == 200:
        data = leetcode_summary.json()  # Parse JSON response
        # print(data)
        prev_total = SubmissionMeta.objects.get(pk=5).total_solved
        if not prev_total:
            if 'totalSolved' in data:
                try:
                    obj, created = SubmissionMeta.objects.update_or_create(
                        total_solved = 0,
                        defaults={'total_solved': data['totalSolved'], 'easy_solved': data['easySolved'], 'medium_solved': data['mediumSolved'], 'hard_solved': data['hardSolved']},
                    )
                except Exception as e:
                    logger.error(f"Error updating leetcodeMeta: {e}")

retrieveLeetMetaStats()