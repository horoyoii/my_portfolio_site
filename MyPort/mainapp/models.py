from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    contents = models.TextField()
    period = models.TextField()
    