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

@admin.action(description="Toggle Published Status")
def make_published(modeladmin, request, queryset):
    for q in queryset:
      q.is_published = not q.is_published
      q.save()

class ProjectAdmin(admin.ModelAdmin):
  list_display = ["title", "link", "image_preview", "is_published"]
  readonly_fields = ['image_preview']
  autocomplete_fields = ['related_skill']
  actions = [make_published]

  fieldsets = [
    (None, {"fields": ["title", "description", "link", "related_skill", "img", "image_preview", "is_published"]})
  ]

admin.site.register(Project, ProjectAdmin)


class ContentAdmin(admin.ModelAdmin):
  list_display = ["title",  "image_preview", "custom_class", "is_published"]
  readonly_fields = ['image_preview']
  actions = [make_published]

  fieldsets = [
    (None, {"fields": ["title", "content",  "img", "wyzywig_content", "image_preview","published", "custom_class"]})
  ]

admin.site.register(Content, ContentAdmin)


class PageAdmin(admin.ModelAdmin):
  list_display = ["title", "slug"]

  fieldsets = [
    (None, {"fields": ["title", "slug", "is_published" ]})
  ]

admin.site.register(Page, PageAdmin)




