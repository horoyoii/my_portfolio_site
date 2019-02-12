from django.forms import ModelForm
from mainapp.models import *
class Form(ModelForm):
    class Meta:
        model = Experience
        fields=['title', 'subtitle', 'contents','period']
