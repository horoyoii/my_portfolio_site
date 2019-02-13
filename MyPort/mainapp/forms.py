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


