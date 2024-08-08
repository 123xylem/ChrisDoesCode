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
from django.conf.urls.static import static
from django.conf import settings
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("cv/", views.cv, name="cv"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about.as_view(), name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin/", admin.site.urls),

] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

#TODO://
# Add debug toolbar for context debugging
#Image field relates to local images when choosing on admin side
# Make Fields better layed out
# Check field functionality
# Link Content model to different pages?
# HTML markup of Home page
# HTML markup of About page
# HTML markup of Courses page
# HTML markup of CV page

#DONE ----------- Show image preview on upload
    #  ------------ Apply to all image fields ^



# Front end styling