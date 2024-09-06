from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.views import generic
from devchris_app.models import *
from django.template.loader import render_to_string

from .forms import contactMeForm
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    FormView,
    UpdateView,
    DetailView
)



def contactMe(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = contactMeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            # cc_myself = form.cleaned_data["cc_myself"]
            subject = f'Django message from: {name}'
            next = request.POST.get('next', '/')

            recipients = ["info@example.com"]
            try:
                send_mail(subject, message, email, recipients)
                data = {
                    'headers': {
                        'status': 200,
                    },
                    'success': True,
                    'message': 'Thank you for your message',
                    'status': 'ok'
                }
                return JsonResponse(data, status=200)

            except Exception as e:
                logger.error(f'Error sending mail, {e} Data: {subject, message, email, recipients}')
                return e
            # print(request)
            # for i in request:
            #     print(i)
            return HttpResponseRedirect(next)
        else:
            return form
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
