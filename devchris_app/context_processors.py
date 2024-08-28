from .models import Page


def published_pages(request):
    pages = Page.objects.filter(is_published=True)
    return {'published_pages': pages}
