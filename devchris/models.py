import datetime
from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

def get_upload_path(instance, filename):
    return 'static/images/{}/{}'.format(datetime.now().strftime('%Y/%m'), filename)

class ImageMixinClass():
  def image_preview(self):
    if self.img and hasattr(self.img, 'url'):
      return mark_safe('<img src="%s" width="150" height="150" />' % (self.img.url))
  image_preview.allow_tags = True
  image_preview.short_description = 'Preview'

class titleMixinClass():
    def __str__(self):
      return self.title



# Text UL Image - for HomePage skills
class Skill(ImageMixinClass, titleMixinClass, models.Model):
    title = models.CharField(max_length=300, default="title")
    img = models.ImageField(upload_to=get_upload_path)
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
  img = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
  custom_class = models.CharField(max_length=300, null=True, blank=True)

class SkillProof(models.Model):
  skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
  description = models.TextField()

