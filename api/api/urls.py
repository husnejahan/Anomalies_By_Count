"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frame/', views.frameList.as_view()),
    path('frame/filter/', views.frameDate.as_view()),
    path('frame/date/', views.frameDateRange.as_view()),
    path('frame/timestamp/', views.frameTimestampRange.as_view()),
    path('frame/<int:pk>/', views.frameDetail.as_view()),
    path('video/', views.videoList.as_view()),
    path('video/<int:pk>/', views.videoDetail.as_view()),
    path('video/<int:videoPK>/frame/', views.videoFrameDetail.as_view()),
    path('video/submit/', views.detectSubmit.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
