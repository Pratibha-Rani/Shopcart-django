# This is a python function ,it takes the request as an argument and it will return dictionary of data as a context
from .models import Category


def menu_links(request): # adding('category.context_processors.menu_links',) in settings templates section we are able to use  these in any templates
    links=Category.objects.all()
    return dict(links=links)