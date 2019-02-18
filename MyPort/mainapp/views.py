from django.shortcuts import render
from mainapp.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import connection
# Create your views here.

def index(request):
    timelineList = TimeLine.objects.all().order_by('subtitle')
    return render(request, 'mainapp/index.html', 
        {'timelineList':timelineList
        })

def profile(request):
    experienceList = Experience.objects.all().order_by('-period') # to use the order by func, needed to import connection from django.db
    skillsList = Skills.objects.all()
    myprofile = MyProfile.objects.get(pk = 1)
    
    return render(request, 'mainapp/profile.html', 
        {'experienceList' : experienceList, 
        'skillsList' : skillsList, 
        'myprofile' : myprofile
        })

def projects(request):
    projectsList = Projects.objects.all()
    return render(request, 'mainapp/projects.html', {'projectsList':projectsList})

def projects_categorized(request, cate, flag):
    if cate == "language":
        projectsList = Projects.objects.filter(language=flag)
    elif cate == "platform":
        projectsList = Projects.objects.filter(platform=flag)
    return render(request, 'mainapp/projects.html', {'projectsList':projectsList})


@login_required
def projects_write(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects')
    else:
        form = ProjectsForm()
    return render(request, 'foradmin/projects_write.html', {'form': form})    





def contact(request):
    
    return render(request, 'mainapp/underconstruction.html')


def underconstruction(request):
     return render(request, 'mainapp/underconstruction.html')



## ===================================================================================================
# Only For Admin
## ===================================================================================================


# ==========================================================
@login_required
def index_about_write(request):
    if request.method == 'POST':
        form = TimeLineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TimeLineForm()
    return render(request, 'foradmin/index_about_write.html', {'form': form})

@login_required
def index_about_update(request ,pk):
    timeline = TimeLine.objects.get(pk = pk)
    form = TimeLineForm(request.POST or None, instance = timeline)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'foradmin/index_about_write.html', {'form':form})

@login_required
def index_about_delete(request, pk):
    timeline = TimeLine.objects.get(pk = pk)
    timeline.delete()
    return HttpResponseRedirect('/')


# ==========================================================
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


@login_required
def profile_skills_update(request, pk):
    skills = Skills.objects.get(pk = pk)
    form = SkillsForm(request.POST or None, instance = skills)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/profile')
    return render(request, 'foradmin/profile_experience_write.html', {'form':form})

@login_required
def profile_skills_delete(request, pk):
    skills = Skills.objects.get(pk = pk)
    skills.delete()
    return HttpResponseRedirect('/profile')





@login_required
def profile_myprofile_edit(request):    
    # db에 생성시 pk는 디폴트로 1부터 시작한다.
    # pk=1의 에러를 피하기 위하여 (시작하기 전) 미리 MyProfile 테이블에 sql문으로 넣어둔다.
    myProfile = MyProfile.objects.get(pk = 1)

    form = MyProfileForm(request.POST or None, instance = myProfile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/profile')
    return render(request, 'foradmin/profile_experience_write.html', {'form':form})

 

#==================================================

@login_required
def projects_update(request, pk):
    project = Projects.objects.get(pk = pk)
    form = ProjectsForm(request.POST or None, instance = project)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/projects')
    return render(request, 'foradmin/projects_write.html', {'form':form})



@login_required
def projects_delete(request, pk):
    project = Projects.objects.get(pk = pk)
    project.delete()
    return HttpResponseRedirect('/projects')