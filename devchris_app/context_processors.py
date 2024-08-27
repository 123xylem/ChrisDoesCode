from .models import Page


def published_pages(request):
    pages = Page.objects.filter(is_published=True)
    print(pages)
    return {'published_pages': pages}
