from django.db import models

class Submission(models.Model):
  answer = models.TextField()
  question = models.TextField()
  rating = models.TextField()
  submitted_date = models.DateTimeField()
  title = models.CharField(max_length=250)
  slug = models.CharField(max_length=100)
  needsUpdate = models.BooleanField(default=True, verbose_name="Up to Date")

  def __str__(self):
    return self.title

class SubmissionMeta(models.Model):
  total_solved = models.IntegerField()
  easy_solved = models.IntegerField()
  medium_solved = models.IntegerField()
  hard_solved = models.IntegerField()
