from decouple import config
import base64
import requests

BEARER_TOKEN = config('BEARER_TOKEN')
LEET_REPO_URL = config('SUB_REPO_URL')
def retrieveSubmissions(max_count=1):
        headers = {'Accept': 'application/vnd.github+json', 'Authorization' : f'token {BEARER_TOKEN}'}
        subs_url = f'{LEET_REPO_URL}/contents/submissions'
        # url2 = 'https://api.github.com/rate_limit'
        # r2 = requests.get(url, headers=headers)
        # print(r2.content)
        # return
        count = 0
        r = requests.get(subs_url, headers=headers)
        submission_folder_urls = []
        q_and_as = []
        for submission_folder in r.json():
            file_dir = submission_folder['name']
            submission_folder_urls.append(file_dir)
            count += 1
            if count > max_count:
                break
        print('folder titles::::::::: ', submission_folder_urls)
        for sub_files in submission_folder_urls:
            question_data = requests.get(subs_url+'/'+sub_files+'/README.md', headers=headers)
            question = base64.b64decode(question_data.json()['content'])
            answer_data = requests.get(subs_url+'/'+sub_files+'/solution.py', headers=headers)
            answer = base64.b64decode(answer_data.json()['content'])
            q_and_as.append({sub_files:[question, answer]})
        print(q_and_as)
