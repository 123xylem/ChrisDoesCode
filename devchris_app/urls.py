from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("cv/", views.cv, name="cv"),
    path('code-with-me/', include('code_app.urls')),
    path("about/", views.about, name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin/", admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

#TODO://
# HTML markup of About page
# HTML markup of Courses page
# HTML markup of CV page
# Add projects and correct content
# Add field for foreignKey Category for content on pages
# Hook up leetcode api? 2 options
        # https://alfa-leetcode-api.onrender.com/G4ZHY5D2Ti/acSubmission
        # https://leetcode-stats-api.herokuapp.com/G4ZHY5D2Ti

# Create app for Leetcode problem display

#DONE ----------- Show image preview on upload
    #  ------------ Apply to all image fields ^
    # ------------- Debug tool bar
    # ------------- # HTML markup of Home page
    # Image field relates to local images when choosing on admin side
    # Link Content model to different pages?
    # Add tiny MCE for CV pip install ckeditor-5
    # Changed App name for clarity
    # Add responsive Nav
    # Add favicon to admin area




# Front end styling