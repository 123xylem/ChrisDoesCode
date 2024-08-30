from .models import  Submission
from django.contrib import admin

class SubmissionAdmin(admin.ModelAdmin):
  #TODO make False show as tick for needsUpdate and change display title of it
  list_display = ["title", "submitted_date", "needsUpdate"]

  fieldsets = [
    (None, {"fields": ["title", "question", "answer"]})
  ]

admin.site.register(Submission, SubmissionAdmin)
