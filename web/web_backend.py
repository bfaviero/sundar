from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page
from django.shortcuts import redirect
from backend.item_api import get_items
from itertools import izip_longest

def login(request):
    context = {}
    context.update(csrf(request))
    return Template("web_login.html", context)

def search(request):
    context = {"grouped_items": _grouper(get_items(request), 3)}
    return Template("search.html", context)

def validate_login(request):
    return redirect("/market")

def _grouper(iterable, n, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)