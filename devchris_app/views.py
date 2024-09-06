from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.views import generic
from devchris_app.models import *
from django.template.loader import render_to_string
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
        context['about_me'] = Content.objects.filter(title='About Me')
        context['testimonials'] = Content.objects.filter(title__startswith="Testimonial")
        context['homepage'] = True
        context['page_title'] = 'Home'
        return context



def about(request):
    context = {
        'about_content': Content.objects.filter(title__startswith="About part"),
        'page_title' : 'About'
    }
    return render(request, 'base.html', context)
      
def cv(request):
    context = {
        'cv_content': Content.objects.filter(title="CV"),
        'page_title' : "CV"
    }
    return render(request, 'base.html', context)

def cvDownload(request):
    cv_content = Content.objects.filter(title='CV').first().wyzywig_content
    response = HttpResponse(cv_content, content_type="text/html")
    response["Content-Disposition"] = 'attachment; filename="chris-cv.doc"'
    return response

def dashboard(request):
    return HttpResponse("Hello, world. You're at dashboard.")


def courses(request):
    return HttpResponse("Hello, world. You're at courses.")
