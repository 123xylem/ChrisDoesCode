from .models import Page
from django.conf import settings
import logging
from .forms import contactMeForm
logger = logging.getLogger(__name__)

def published_pages(request):
    pages = Page.objects.filter(is_published=True)
    return {'published_pages': pages}

def site_details(request):
    return {
    'MY_EMAIL': settings.MY_EMAIL,
    'MY_LINKEDIN': settings.MY_LINKEDIN,
    'MY_GITHUB': settings.MY_GITHUB,
    }

def contact_form_init(request):
    contact_form = contactMeForm()
    return {'contact_form' : contact_form }
