import datetime
from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe
from filer.fields.image import FilerImageField
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


def get_upload_path(instance, filename):
    return 'static/images/{}/{}'.format(datetime.now().strftime('%Y/%m'), filename)

class ImageMixinClass():
  def image_preview(self):
      html= ""
      for field in self._meta.fields:
          field_value = getattr(self, field.name)
          if isinstance(field, models.ImageField):
              if field_value:
                  url = field_value.url if hasattr(field_value, 'url') else field_value
                  html += '<img src="%s" width="150" height="150" />' % url
          # Preview django-filer img?
          elif isinstance(field, FilerImageField):
              if field_value and hasattr(field_value, 'url'):
                  html += '<img src="%s" width="150" height="150" />' % field_value.url

      return mark_safe(html)
    # if self.img and hasattr(self.img, 'url'):

    #   return mark_safe('<img src="%s" width="150" height="150" />' % (self.img.url))
  image_preview.allow_tags = True
  image_preview.short_description = 'Preview'

class titleMixinClass():
    def __str__(self):
      return self.title



# Text UL Image - for HomePage skills
class Skill(ImageMixinClass, titleMixinClass, models.Model):
    title = models.CharField(max_length=300, default="title")
    # img = models.ImageField(upload_to=get_upload_path)
    img = FilerImageField(related_name="skill_img", null=True, blank=True, on_delete=models.CASCADE)
    # test_img = FilerImageField(related_name="book_covers", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
      ordering = ["title"]

 # TEXT IMAGE LINK - FOr: homepageProjects
class Project(models.Model, ImageMixinClass, titleMixinClass):
    description = models.TextField()
    title = models.CharField(max_length=300, default='Project Title')
    link = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to=get_upload_path)
    related_skill = models.ManyToManyField(Skill, blank=True)
    # models.ManyToManyField(related_query_name='title')
    # related_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)


# // TEXT/ IMAGES - For: About Me - Testimonials
class Content(models.Model, ImageMixinClass, titleMixinClass):
  title = models.CharField(max_length=250, default="title")
  content = models.TextField()
  wyzywig_content = CKEditor5Field('Text', config_name='extends')
  img = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
  custom_class = models.CharField(max_length=300, null=True, blank=True)

class SkillProof(models.Model):
  skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='proofs')
  description = models.TextField()

class Page(models.Model, titleMixinClass):
  title = models.CharField(max_length=250)
  is_published = models.BooleanField(default=False)
  slug = models.SlugField(unique=True, blank=True, max_length=255)

  def save(self, *args, **kwargs):
      if not self.slug:
          self.slug = slugify(self.title)
          # Ensure uniqueness
          original_slug = self.slug
          queryset = Page.objects.filter(slug=self.slug).exclude(id=self.id)
          count = 1
          while queryset.exists():
              self.slug = f'{original_slug}-{count}'
              count += 1
      super(Page, self).save(*args, **kwargs)

  def get_absolute_url(self):
      return f"/{slugify(self.slug)}/"
