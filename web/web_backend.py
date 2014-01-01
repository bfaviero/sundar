from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page

def login(request):
    context = {}
    context.update(csrf(request))
    return Template("web_login.html", context)

def search(request):
    return Template("search.html")

