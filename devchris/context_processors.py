from .models import Page


def published_pages(request):

    pages = Page.objects.filter(is_published=True)
    print(pages.__dict__)
    return {'published_pages': pages}
