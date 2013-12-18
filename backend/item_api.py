from templating import Template, error_page
from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf


def index(request):
    return HttpResponse("SUCCESS INDEX")

def get_item(request):
    return HttpResponse("SUCCESS GET_ITEM")

def update_item(request):
    return HttpResponse("SUCCESS UPDATE ITEM")

def delete_item(request):
    return HttpResponse("SUCCESS DELETE ITEM")

def get_items(request):
    return HttpResponse("SUCCESS GET ITEMS")
