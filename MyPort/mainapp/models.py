from django.db import models

# For auto file delete======
import os
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
#======


# Create your models here.
# pk is created automatically...

class Experience(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    contents = models.TextField()
    period = models.TextField()
    
class Skills(models.Model):
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=200) # 수준
    contents = models.TextField()           # 수준에 대한 상세 설명
    type = models.TextField()               # 어떤 종류의 스킬인가 ? language or tools or frameworks 등

    

class MyProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    position = models.TextField()
    intro = models.TextField()
    interests = models.TextField()
    
class TimeLine(models.Model):
    date = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle =  models.TextField()
    contents =  models.TextField()
    image = models.FileField(upload_to='documents/About/img/')
    
    # it will be deleted 
    cover = models.ImageField(upload_to='About/cover/',  null = True, blank = True) 
 
# These two auto-delete files from filesystem when they are unneeded:
# Reference : https://stackoverflow.com/questions/16041232/django-delete-filefield

@receiver(models.signals.post_delete, sender=TimeLine)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `TimeLine` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=TimeLine)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `TimeLine` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = TimeLine.objects.get(pk=instance.pk).image
    except TimeLine.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)