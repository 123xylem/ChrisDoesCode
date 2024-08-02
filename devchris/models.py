import datetime
from django import forms
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Text UL Image - for HomePage skills
class Skill(models.Model):
    skill_title = models.CharField(max_length=300)
    img = models.ImageField(upload_to ='static/images/% Y/% m/')
    skill_proof = models.CharField(max_length=600, null=True, blank=True)

    def __str__(self):
      return self.skill_title


    #Set Admin Display preferences
    # @admin.display(
    #     boolean=True,
    #     ordering="pub_date",
    #     description="Published recently?",
    # )
    

 # TEXT IMAGE LINK - FOr: homepageProjects
class Project(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=300, default='Project Title')
    link = models.CharField(max_length=300, null=True, blank=True)
    img = models.ImageField(upload_to ='static/images/{% Y/% m/}')
    related_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title


# // TEXT/ IMAGES - For: About Me - Testimonials
class Content(models.Model):
  content = models.TextField()
  img = models.ImageField(upload_to ='static/images/% Y/% m/', null=True, blank=True)
  custom_class = models.CharField(max_length=300, null=True, blank=True)

class SkillProof(models.Model):
  skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
  description = models.TextField()


# q2 = Question(question_text="Chris's Question is are you good?", pub_date=timezone.now())