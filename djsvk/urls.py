"""
URL configuration for djsvk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from djsvk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about-us/',views.aboutus),
    path('course/',views.course),
    #path('course/<int:courseid>',views.coursed),  #This is for integer type
    #path('course/<str:courseid>',views.coursed),  #This is for string type
    #path('course/<slug:courseid>',views.coursed)  #This is for slug type like abc_dbbd_dd
    path('course/<courseid>',views.coursed),
    path('aboutus/',views.about),
    path('userform/',views.userform)
    #This is for any type
]
