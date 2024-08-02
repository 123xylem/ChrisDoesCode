"""
URL configuration for devchris project.

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

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("cv/", views.cv, name="cv"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about.as_view(), name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin/", admin.site.urls),

]


#TODO://
#Image field relates to local images when choosing on admin side
# Make Fields better layed out
# Check field functionality

# HTML markup of Home page
# HTML markup of About page
# HTML markup of Courses page
# HTML markup of CV page





# Front end styling