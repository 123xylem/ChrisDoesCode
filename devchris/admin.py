from .models import  Skill, Project, Content, SkillProof
from django.contrib import admin


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3


# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ["question_text", "pub_date",  "was_published_recently"]
#     list_filter = ["pub_date"]
#     search_fields = ["question_text"]

#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
#     ]
#     inlines = [ChoiceInline]


# admin.site.register(Question, QuestionAdmin)


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class SkillInline(admin.TabularInline):
    model = SkillProof
    extra = 3


class SkillAdmin(admin.ModelAdmin):
  list_display = ["skill_title", "skill_proof",  "img"]
  search_fields = ["skill_title"]
  fieldsets = [
    (None, {"fields": ["skill_title", "skill_proof",  "img"]})
  ]
  inlines = [ProjectInline]
  inlines = [SkillInline]

admin.site.register(Skill, SkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
  list_display = ["title", "description", "link",  "img"]
  fieldsets = [
    (None, {"fields": ["title", "description", "link",  "img"]})
  ]

admin.site.register(Project, ProjectAdmin)


class ContentAdmin(admin.ModelAdmin):
  list_display = ["content",  "img", "custom_class"]
  fieldsets = [
    (None, {"fields": ["content",  "img", "custom_class"]})
  ]

admin.site.register(Content, ContentAdmin)





