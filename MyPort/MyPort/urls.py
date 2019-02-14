"""MyPort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('profile/', profile, name='profile'),
    path('profile/experience/write', profile_experience_write, name='pew'),
    path('profile/experience/edit/<int:pk>', profile_experience_update, name='peu'),
    path('profile/experience/delete/<int:pk>', profile_experience_delete, name='ped'),
    path('profile/skills/write', profile_skills_write, name='pes'),
    path('profile/myprofile/edit', profile_myprofile_edit, name='pme'),
    path('index/about/write', index_about_write, name='iaw'),
    path('profile/timeline/edit/<int:pk>', index_about_update, name='iau'),
    path('profile/timeline/delete/<int:pk>', index_about_delete, name='iad'),

]

# this is needed to serve the sources 
# and with this, don't need to indicate all the path of the stored data
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
