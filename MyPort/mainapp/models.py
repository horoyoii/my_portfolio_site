from django.db import models

# For auto file delete======
import os
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
import requests
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
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


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    sep = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)



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



class engTimeLine(models.Model):
    date = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle =  models.TextField()
    contents =  models.TextField()
    image = models.FileField(upload_to='documents/About/img/eng/')
    
 
# These two auto-delete files from filesystem when they are unneeded:
# Reference : https://stackoverflow.com/questions/16041232/django-delete-filefield

@receiver(models.signals.post_delete, sender=engTimeLine)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `TimeLine` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=engTimeLine)
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


#====================================================================================================
# Projects 
#====================================================================================================


class Projects(models.Model):
    CLANGUAGE ='CL'
    CPLUSPLUS ='CP'
    JAVA ='JV'
    PYTHON ='PY'
    ELSE = 'ES'
    LANGUAGE_CHOICE =(
        (CLANGUAGE,'C language'),
        (CPLUSPLUS,'Cpp'),
        (JAVA,'Java'),
        (PYTHON,'Python'),
        (ELSE, 'Else'),
    )   

    WEB = 'WB'
    APP = 'AP'
    DESKTOP ='DS'
    IMBE = 'IM'
    ETC ='ET'
    CLASS_CHOICE=(
        (WEB,'Web'),
        (APP,'Mobile App'),
        (DESKTOP, 'DeskTop App'),
        (IMBE,'Imbedded'),
        (ETC, 'ETC')
    )

    date = models.DateField(help_text="ex) 2017-02-28")
    subtitle = models.CharField(max_length=200, help_text="썸네일과 함께 보여질 제목")
    subContents = models.TextField(help_text="썸네일과 함께 보여질 간략한 내용")
    #TODO: to thumbnail generator
    imageURLGit = models.TextField(default ="https://user-images.githubusercontent.com/34915108/53049248-069d5580-34da-11e9-81be-d683105b0f7d.gif", help_text="* 썸네일 사진 : 사진 직접 올리지말고 url을 올림")
    con = MarkdownxField(help_text="* 보여질 내용물 : markdown으로 작성")
    language = models.CharField(
        max_length=2, 
        choices=LANGUAGE_CHOICE,
        default=CLANGUAGE,
        )
    platform = models.CharField(
        max_length=2, 
        choices=CLASS_CHOICE,
        default=ETC,
        )
    show_public = models.BooleanField(default=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.con)

    def __str__(self):
        return self.name