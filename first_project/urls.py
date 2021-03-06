"""first_project URL Configuration

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
from first_app import views
from django.urls import include


urlpatterns = [
    path('',include('first_app.urls')),
    path('admin/', admin.site.urls),
    path('user_logout/', views.user_logout,name='user_logout'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('exam/',views.Interview_Exam,name='Interview_Exam'),
    path('InterviewDetail/', views.Interview_Detail_Exam,name='Interview_Detail_Exam'),
    path('videorecorder/', views.video_recorder,name='video_recorder'),
    path('', views.index,name='index'),
]
