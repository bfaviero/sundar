from templating import Template, error_page
from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf

def create_supplier(request):
    return HttpResponse("SUCCESS create_supplier ")

def update_supplier(request):
    return HttpResponse("SUCCESS update_supplier ")

def delete_supplier(request):
    return HttpResponse("SUCCESS delete_supplier ")

def login_supplier(request):
    return HttpResponse("SUCCESS login_supplier ")