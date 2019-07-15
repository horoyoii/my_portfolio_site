from django.shortcuts import render
from mainapp.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db import connection
# Create your views here.

def index(request):
    lan = request.COOKIES.get('language', 'kor') # default is kor // language 라는 key값이 없다면 kor을 return한다.
    if(lan == 'kor'):
        timelineList = TimeLine.objects.all().order_by('subtitle')
        response = render(request, 'mainapp/index.html', 
            {'timelineList':timelineList
            })
        response.set_cookie('language', 'kor')
        return response

    elif(lan == 'eng'):
        timelineList = engTimeLine.objects.all().order_by('subtitle')
        response = render(request, 'mainapp/index.html', 
            {'timelineList':timelineList
            })
        response.set_cookie('language', 'eng')
        return response        

def profile(request):
    lan = request.COOKIES.get('language', 'kor')
    if(lan =='kor'):
        myprofile = MyProfile.objects.get(pk = 1)
        univ = '성균관 대학교'
        highSchool = '대연 고등학교'
        location = '부산'
    elif(lan =='eng'):
        myprofile = MyProfile.objects.get(pk = 2)
        univ = 'sungkyunkwan university'
        highSchool = 'DeaYeon HighSchool'
        location ='Busan'
    experienceList = Experience.objects.all().order_by('-period') # to use the order by func, needed to import connection from django.db
    skillsList = Skills.objects.all()
    lectureList = Lecture.objects.all()
    

    return render(request, 'mainapp/profile.html', 
        {'experienceList' : experienceList, 
        'skillsList' : skillsList, 
        'myprofile' : myprofile,
        'univ' : univ,
        'highSchool' : highSchool,
        'location' : location,
        'lectureList':lectureList
        })

def projects(request):
    projectsList = Projects.objects.all()
    return render(request, 'mainapp/projects.html', {'projectsList':projectsList})

def projects_categorized(request, cate, flag):
    if cate == "language":
        projectsList = Projects.objects.filter(language=flag)
    elif cate == "platform":
        projectsList = Projects.objects.filter(platform=flag)
    return render(request, 'mainapp/projects.html', {'projectsList':projectsList, 'maxim':getMaxim(flag)})

MaximList = {"CL" : "“A C program is like a fast dance \n on a newly waxed dance floor by people carrying razors.” \n- Alan Jay Perlis",
    "CP" : "Who would dare to say that he has masterd C++?",
    "PY" : "Simple is better than Complex",
    "JV" : "“Fine, Java MIGHT be a good example of what a programming language should be like. \nBut Java applications are good examples of what applications SHOULDN’T be like.” \n- pixadel",
    "DS" : "“Learning to program has no more to do with designing interactive software \nthan learning to touch type has to do with writing poetry” \n- Alan Kay",
    "WB" : "",
    "AP" :"",
    "IM" : "",
    "ET" : "“Most good programmers do programming \nnot because they expect to get paid or get adulation by the public, \nbut because it is fun to program.” \n- Charles Babbage"
    }

def getMaxim(flag):
    global MaximList
    return MaximList[flag]

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
@login_required
def conn(request):
    if request.method == 'POST':
        form = MyProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
    else:
        form = MyProfileForm()
    return render(request, 'foradmin/index_about_write.html', {'form': form})       

# ==========================================================


@login_required
def profile_lecture_write(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/#education')
    else:
        form = LectureForm()
    return render(request, 'foradmin/index_about_write.html', {'form': form})



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
def index_about_engwrite(request):
    if request.method == 'POST':
        form = engTimeLineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = engTimeLineForm()
    return render(request, 'foradmin/index_about_write.html', {'form': form})


@login_required
def index_about_update(request ,pk):
    lan = request.COOKIES.get('language')
    if(lan == 'kor'):          
        timeline = TimeLine.objects.get(pk = pk)
        form = TimeLineForm(request.POST or None, instance = timeline)
    elif(lan =='eng'):
        timeline = engTimeLine.objects.get(pk = pk)
        form = engTimeLineForm(request.POST or None, instance = timeline)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'foradmin/index_about_write.html', {'form':form})

@login_required
def index_about_delete(request, pk):
    lan = request.COOKIES.get('language')
    if(lan == 'kor'):          
        timeline = TimeLine.objects.get(pk = pk)
    if(lan == 'eng'):          
        timeline = engTimeLine.objects.get(pk = pk)
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
    lan = request.COOKIES.get('language')
    if(lan == 'kor'):      
        myProfile = MyProfile.objects.get(pk = 1)
    elif(lan=='eng'):
        myProfile = MyProfile.objects.get(pk = 2)
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






# ====================================================================================
# 다국어 지원 기능
# ====================================================================================

def index_kor(request):
    timelineList = TimeLine.objects.all().order_by('subtitle')
    response = render(request, 'mainapp/index.html', 
        {'timelineList':timelineList
        })    
    lan = request.COOKIES.get('language')
    if(lan == 'eng'):
        response.set_cookie('language', 'kor')
    return response


def index_eng(request):
    timelineList = engTimeLine.objects.all().order_by('subtitle')
    response = render(request, 'mainapp/index.html', 
        {'timelineList':timelineList
        })    
    lan = request.COOKIES.get('language')
    if(lan == 'kor'):
        response.set_cookie('language', 'eng')
    return response

def profile_kor(request):
    myprofile = MyProfile.objects.get(pk = 1)
    univ = '성균관 대학교'
    highSchool = '대연 고등학교'
    location = '부산'    
    experienceList = Experience.objects.all().order_by('-period') # to use the order by func, needed to import connection from django.db
    skillsList = Skills.objects.all()
    response = render(request, 'mainapp/profile.html', 
        {'experienceList' : experienceList, 
        'skillsList' : skillsList, 
        'myprofile' : myprofile,
        'univ' : univ,
        'highSchool' : highSchool,
        'location' : location,
        })

    lan = request.COOKIES.get('language')
    if(lan == 'eng'):
        response.set_cookie('language', 'kor')
    return response


def profile_eng(request):
    myprofile = MyProfile.objects.get(pk = 2)
    univ = 'sungkyunkwan university'
    highSchool = 'DeaYeon HighSchool'
    location ='Busan'
    experienceList = Experience.objects.all().order_by('-period') # to use the order by func, needed to import connection from django.db
    skillsList = Skills.objects.all()

    response = render(request, 'mainapp/profile.html', 
        {'experienceList' : experienceList, 
        'skillsList' : skillsList, 
        'myprofile' : myprofile,
        'univ' : univ,
        'highSchool' : highSchool,
        'location' : location,
        })

    lan = request.COOKIES.get('language')
    if(lan == 'kor'):
        response.set_cookie('language', 'eng')
    return response    