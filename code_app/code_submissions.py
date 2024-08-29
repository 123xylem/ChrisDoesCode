from decouple import config
import base64
import requests
from .models import Submission
from datetime import datetime


BEARER_TOKEN = config('BEARER_TOKEN')
SUB_REPO_URL = config('SUB_REPO_URL')
SUB_META_URL = config('SUB_META_URL')
headers = {'Accept': 'application/vnd.github+json', 'Authorization' : f'token {BEARER_TOKEN}'}
subs_url = f'{SUB_REPO_URL}/contents/submissions'

def validateQaData(data):
    if not data:
        print('invalid data:', data)
        return False
    if 'content' in data.json():
        return base64.b64decode(data.json()['content'])
    else:
        print('This question has no content?', data.json())
        return False

def getQaDataFromFiles(file_dir, filename):
    print(subs_url+'/'+file_dir+'/'+filename)
    requests.get(subs_url+'/'+file_dir+'/'+filename, headers=headers)

def addSubmissionsToDbOnMetaMatch(submissions:list):
    for q_a in submissions:
        for k, v in q_a.items():
            k = ''.join([char for char in k if char.isalpha() or char == '-'])
            title = ' '.join([word.capitalize() for word in k.split('-')]).strip()
            # print('key:', title, len(title))
            question = v[0]
            answer = v[1]
            # print(Submission.objects.get(pk=1), title)
            Submission.objects.filter(title=title, needsUpdate=True).update(question=question, answer=answer, needsUpdate=False)


def retrieveSubmissionsFromRepo(max_count=10):
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
        question_data =getQaDataFromFiles(sub_files, 'README.md')
        answer_data = getQaDataFromFiles(sub_files, 'solution.py')
        if question_data and answer_data:
            question = validateQaData(question_data)
            answer = validateQaData(answer_data)
            if answer and question:
                q_and_as.append({sub_files:[question, answer]})

    if q_and_as:
        addSubmissionsToDbOnMetaMatch(q_and_as)


def createSubmissionFromMeta(submissions:list):
    # print(submissions)
    for sub in submissions:
        new_title = sub['title']
        new_date = sub['timestamp']
        try:
            submission = Submission.objects.get(title=new_title)
            if submission.submitted_date != new_date:
                submission.submitted_date = new_date
                submission.needsUpdate = True
                submission.save()
            else:
                # The data is identical; no need to update
                print("No update needed, data is identical")
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
        res1 = requests.get(SUB_META_URL)
        # res2 = requests.get('https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti')
        if res1.status_code == 200:
              data = res1.json()
              submissions = data['submission']
            #   print(type(submissions))
              filterSubmissionMeta(submissions)

