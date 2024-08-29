from .models import  Submission
from django.contrib import admin

class SubmissionAdmin(admin.ModelAdmin):
  list_display = ["title", "rating", "submitted_date"]

  fieldsets = [
    (None, {"fields": ["title", "question", "answer"]})
  ]

admin.site.register(Submission, SubmissionAdmin)
