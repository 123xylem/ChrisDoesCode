from django.db import models

class Submission(models.Model):
  answer = models.TextField()
  question = models.TextField()
  rating = models.TextField()
  submitted_date = models.DateTimeField()
  title = models.CharField(max_length=250)
  needsUpdate = models.BooleanField(default=True)

  def __str__(self):
    return self.title

