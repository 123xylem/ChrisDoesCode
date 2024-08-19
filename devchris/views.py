from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from devchris.models import *
import json

from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    FormView,
    UpdateView,
    DetailView
)

class index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)
        context['skill_list'] = Skill.objects.all()
        context['project_list'] = Project.objects.all()
        context['content_list'] = Content.objects.filter(title='About Me')
        context['testimonials'] = Content.objects.filter(title__startswith="Testimonial")

        return context



def about(request):
    context = {
        'content_list': Content.objects.filter(title__startswith="About part")
    }
    return render(request, 'base.html', context)
      
def cv(request):
    context = {
        'content_list': Content.objects.filter(title="CV")
    }
    return render(request, 'base.html', context)

def dashboard(request):
    return HttpResponse("Hello, world. You're at dashboard.")


def courses(request):
    return HttpResponse("Hello, world. You're at courses.")


# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         pass

# class DetailView(generic.DetailView):
#     template_name = "polls/detail.html"
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         pass
