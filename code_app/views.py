from devchris_app.models import *
import requests, logging
from decouple import config
from datetime import datetime
from .code_submissions import retrieveSubmissionsFromRepo, retrieveSubmissionMetaFromLeetCode
from .models import Submission, SubmissionMeta
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    FormView,
    UpdateView,
    DetailView
)
from .utils import *

logger = logging.getLogger(__name__)

# LEET_STATS_URL = config('LEET_STATS_URL')
class codePage(TemplateView):
    template_name = "code_app/code_page.html"
    
    def get_context_data(self, **kwargs):    
        leetcode_meta = SubmissionMeta.objects.all()
        total_solved = easy_solved = medium_solved = hard_solved = 0

        for meta in leetcode_meta:
            total_solved += meta.total_solved
            easy_solved += meta.easy_solved
            medium_solved += meta.medium_solved
            hard_solved += meta.hard_solved

        formatted_meta = {
            'Total Solved': total_solved,
            'Easy Solved': easy_solved,
            'Mid Solved': medium_solved,
            'Hard Solved': hard_solved
        }

        submissions = Submission.objects.all().order_by('id')
        for sub in submissions:
            sub.question = clean_text(sub.question)
            sub.answer = clean_text(sub.answer, True)
            print(sub.title)
        return {'leetcode_meta':formatted_meta, 'submissions': submissions}
        # https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission
        # https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti
