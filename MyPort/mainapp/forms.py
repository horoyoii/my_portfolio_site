from django.forms import ModelForm
from mainapp.models import *
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields=['title', 'subtitle', 'contents','period']


class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields=['title', 'grade', 'contents','type']

class MyProfileForm(ModelForm):
    class Meta:
        model = MyProfile
        fields=['name', 'email', 'position', 'intro','interests']

class TimeLineForm(ModelForm):
    class Meta:
        model = TimeLine
        fields=['date', 'title', 'subtitle', 'contents', 'image', 'cover']

class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        fields=['date', 'subtitle','subContents','imageURLGit','language', 'platform']
        # label, widget을 추가하여 form을 꾸밀 수 있다.