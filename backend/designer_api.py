from templating import Template, error_page
from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf

def create_designer(request):
    return HttpResponse("SUCCESS create_designer ")

def update_designer(request):
    return HttpResponse("SUCCESS update_designer ")

def delete_designer(request):
    return HttpResponse("SUCCESS delete_designer ")

def login_designer(request):
    return HttpResponse("SUCCESS login_designer")
