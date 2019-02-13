from django.shortcuts import render
from mainapp.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import connection
# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {})

def profile(request):
    experienceList = Experience.objects.all().order_by('-period') # to use the order by func, needed to import connection from django.db
    skillsList = Skills.objects.all()
    return render(request, 'mainapp/profile.html', {'experienceList' : experienceList, 'skillsList' : skillsList})











## ===================================================================================================
# Only For Master
## ===================================================================================================



@login_required
def profile_experience_write(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/profile') # need url
    else:
        form = ExperienceForm()
    
    return render(request, 'foradmin/profile_experience_write.html', {'form':form})

@login_required
def profile_experience_update(request, pk):
    experience = Experience.objects.get(pk = pk)
    form = ExperienceForm(request.POST or None, instance = experience)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/profile')
    return render(request, 'foradmin/profile_experience_write.html', {'form':form})

@login_required
def profile_experience_delete(request, pk):
    experience = Experience.objects.get(pk = pk)
    experience.delete()
    return HttpResponseRedirect('/profile')


@login_required
def profile_skills_write(request):
    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/profile') # need url
    else:
        form = SkillsForm()
    
    return render(request, 'foradmin/profile_experience_write.html', {'form':form})
