from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls
app_name = "code_app"

urlpatterns = [
    path("", views.codePage.as_view(), name="codePage")
] + debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)