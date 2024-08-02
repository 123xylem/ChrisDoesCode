from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

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
      # content = {
      #     "title" : "Web Dev Chris",
      #     "content" : "Web Dev Chris is amazing",
      # }
      def get_content(self, content):
        """Return the last five published questions."""
        return HttpResponseRedirect(reverse("/", args=(content,)))
      
      def get_context_data(self,*args, **kwargs):
        content = {
            "title" : "Web Dev Chris",
            "content" : "Web Dev Chris is amazing",
        }
        return content



class about(TemplateView):
      template_name = "about.html"
      content = {
          "title" : "Web Dev Chris",
          "content" : "Web Dev Chris is amazing",
      }
      def get_content(self, content):
        """Return the last five published questions."""
        return HttpResponseRedirect(reverse("/", args=(content,)))
      
def cv(request):
    return HttpResponse("Hello, world. You're at cv.")

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
