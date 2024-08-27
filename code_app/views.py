from devchris_app.models import *
import requests
from datetime import datetime


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

    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)
        res1 = requests.get('https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission')
        # res2 = requests.get('https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti')
        if res1.status_code == 200:
              data = res1.json()  # Parse JSON response
              # data2 = res1.json()  # Parse JSON response
              print(data)
              count = data['count']
              submissions = data['submission']
              filtered_submissions = [sub for sub in submissions if sub['statusDisplay'] == 'Accepted']
              for submission in filtered_submissions:
                submission['timestamp'] = datetime.fromtimestamp(int(submission['timestamp']))                    
     
        return {'count':count, 'solutions': filtered_submissions}
        # https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission
        # https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti

# {'count': 12, 'submission': [{'title': 'Majority Element', 'titleSlug': 'majority-element', 'timestamp': '1724143474', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Top K Frequent Elements', 'titleSlug': 'top-k-frequent-elements', 'timestamp': '1723037216', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Valid Sudoku', 'titleSlug': 'valid-sudoku', 'timestamp': '1722865967', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Product of Array Except Self', 'titleSlug': 'product-of-array-except-self', 'timestamp': '1722853642', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Top K Frequent Elements', 'titleSlug': 'top-k-frequent-elements', 'timestamp': '1722507056', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Group Anagrams', 'titleSlug': 'group-anagrams', 'timestamp': '1722459132', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Remove Element', 'titleSlug': 'remove-element', 'timestamp': '1722436160', 'statusDisplay': 'Accepted', 'lang': 'python3'}, {'title': 'Valid Anagram', 'titleSlug': 'valid-anagram', 'timestamp': '1722431381', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Majority Element', 'titleSlug': 'majority-element', 'timestamp': '1722420680', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Two Sum', 'titleSlug': 'two-sum', 'timestamp': '1722417623', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Contains Duplicate', 'titleSlug': 'contains-duplicate', 'timestamp': '1722242821', 'statusDisplay': 'Accepted', 'lang': 'python'}, {'title': 'Concatenation of Array', 'titleSlug': 'concatenation-of-array', 'timestamp': '1722241853', 'statusDisplay': 'Accepted', 'lang': 'python'}]}