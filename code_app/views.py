from devchris_app.models import *
import requests
from datetime import datetime
from .code_submissions import retrieveSubmissionsFromRepo, retrieveSubmissionMetaFromLeetCode
from .models import Submission
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    FormView,
    UpdateView,
    DetailView
)

class codePage(TemplateView):
    template_name = "code_app/code_page.html"
    

    #TODO: Manual retrieval of submission and meta MOVE THIS TO CRON
    # submissions = retrieveSubmissionsFromRepo(20)
    # sub_meta = retrieveSubmissionMetaFromLeetCode()
    
    def get_context_data(self, **kwargs):    
        # context = super().get_context_data(**kwargs)
        # res1 = requests.get('https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission')
        #TODO make this a leetcode summary Model
        #TODO call it with automated worker
        leetcode_summary = requests.get('https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti')
        if leetcode_summary.status_code == 200:
              data = leetcode_summary.json()  # Parse JSON response
              # data2 = res1.json()  # Parse JSON response
              code_meta = {}
              code_meta['totalSolved'] = data['totalSolved']
              code_meta['easySolved'] = data['easySolved']
              code_meta['mediumSolved'] = data['mediumSolved']
              code_meta['hardSolved'] = data['hardSolved']
              code_meta['acceptanceRate']= data['acceptanceRate']
              submissions = Submission.objects.all()
        return {'code_meta':code_meta, 'submissions': submissions}
        # https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission
        # https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti

# {'count': 12, 'submission': [{'title': 'Majority Element', 'titleSlug': 'majority-element', 'timestamp': '1724143474', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Top K Frequent Elements', 'titleSlug': 'top-k-frequent-elements', 'timestamp': '1723037216', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Valid Sudoku', 'titleSlug': 'valid-sudoku', 'timestamp': '1722865967', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Product of Array Except Self', 'titleSlug': 'product-of-array-except-self', 'timestamp': '1722853642', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Top K Frequent Elements', 'titleSlug': 'top-k-frequent-elements', 'timestamp': '1722507056', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Group Anagrams', 'titleSlug': 'group-anagrams', 'timestamp': '1722459132', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Remove Element', 'titleSlug': 'remove-element', 'timestamp': '1722436160', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Valid Anagram', 'titleSlug': 'valid-anagram', 'timestamp': '1722431381', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Majority Element', 'titleSlug': 'majority-element', 'timestamp': '1722420680', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Two Sum', 'titleSlug': 'two-sum', 'timestamp': '1722417623', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Contains Duplicate', 'titleSlug': 'contains-duplicate', 'timestamp': '1722242821', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Concatenation of Array', 'titleSlug': 'concatenation-of-array', 'timestamp': '1722241853', 'statusDisplay': 'Accepted', 'lang': 'python'}]}