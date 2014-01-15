from utils import request_arg, optional_request_arg
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page
from django.shortcuts import redirect
from backend.item_api import *
from backend.models import *
from itertools import izip_longest
from django.shortcuts import render
from forms import UserForm

def login(request):
    form = UserForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("market"))
    return render(request, 'web_login.html', {'form': form })


@login_required
def item(request, item_id):
	context =  {"item": get_item(item_id=item_id)}
	return Template("item.html", context)

@login_required
def market(request):
    context = {"items": get_all_items(request)}
    return Template("items.html", context)