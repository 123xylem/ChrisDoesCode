from .models import  Submission
from django.contrib import admin
from django.utils.html import format_html

class SubmissionAdmin(admin.ModelAdmin):
  list_display = ["title", "submitted_date", "up_to_date"]
  fieldsets = [
    (None, {"fields": ["title", "question", "answer"]})
  ]
  # Swap True (✓) with False (×)
  def up_to_date(self, obj):
    return not obj.needsUpdate
  up_to_date.boolean = True 

admin.site.register(Submission, SubmissionAdmin)
