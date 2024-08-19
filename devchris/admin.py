from .models import  Skill, Project, Content, SkillProof, Page
from django.contrib import admin
from django.utils.text import slugify

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class SkillInline(admin.TabularInline):
    model = SkillProof
    extra = 3


class SkillAdmin(admin.ModelAdmin):
  list_display = ["title",  "image_preview"]
  search_fields = ["title"]
  readonly_fields = ['image_preview']
  fieldsets = [
    (None, {"fields": ["title", "img", "image_preview"]})
  ]
  inlines = [ProjectInline]
  inlines = [SkillInline]

admin.site.register(Skill, SkillAdmin)

class ProjectAdmin(admin.ModelAdmin):
  list_display = ["title", "link", "image_preview"]
  readonly_fields = ['image_preview']
  autocomplete_fields = ['related_skill']

  fieldsets = [
    (None, {"fields": ["title", "description", "link", "related_skill", "img", "image_preview"]})
  ]

admin.site.register(Project, ProjectAdmin)


class ContentAdmin(admin.ModelAdmin):
  list_display = ["title",  "image_preview", "custom_class"]
  readonly_fields = ['image_preview']
  fieldsets = [
    (None, {"fields": ["title", "content",  "img", "image_preview", "custom_class"]})
  ]

admin.site.register(Content, ContentAdmin)


class PageAdmin(admin.ModelAdmin):
  list_display = ["title", "slug"]

  fieldsets = [
    (None, {"fields": ["title", "slug", "is_published" ]})
  ]

admin.site.register(Page, PageAdmin)




