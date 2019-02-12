from django.db import models

# Create your models here.
# pk is created automatically...

class Experience(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    contents = models.TextField()
    period = models.TextField()
    