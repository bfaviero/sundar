from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from backend.models import Supplier, Item
from backend.item_api import get_items
from django.forms.models import model_to_dict
from constants import *
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.signals import user_logged_in, user_logged_out
from web.forms import UserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_in
from django.utils import simplejson

def login(request):
    context = {}
    context.update(csrf(request))
    form = UserForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            log_in(request, user)
            return redirect(reverse("edit_product"))

    context['form'] = form
    return render(request, 'login.html', context)

def render_edit_product(request):
    item_id = optional_request_arg(request, "item_id")
    if item_id:
        item = Item.objects.get(id=item_id)
    else:
        item = Item()
    context = {"item": model_to_dict(item),
               "wholesale_price_units": WHOLESALE_PRICE_UNITS,
               "fabric_width_units": FABRIC_WITDH_UNITS,
               "basic_material_types": BASIC_MATERIAL_TYPES,
               "textile_types": TEXTILE_TYPES,
               "weave_types": WEAVE_TYPES,
               "fabric_weight_units": FABRIC_WEIGHT_UNITS,
               "fiber_types": FIBER_TYPES,
               "textile_types_list": simplejson.dumps(TEXTILE_TYPES_LIST),
               "countries": simplejson.dumps(countries)}
    context.update(csrf(request))
    return Template("edit_product.html", context)

def render_product_list(request):
    #TO TURN ACCOUNTS ON, exhange this line with next line:
    context = {"items": get_items(request)}
    #context.update(csrf(request))
    return Template("product_list.html", context)

def render_sign_up(request):
    context = {}
    context.update(csrf(request))
    return Template("signup.html", context)

def example(request):
    context = {}
    context.update(csrf(request))
    return Template("Example.html", context)

def camera(request):
    context = {}
    context.update(csrf(request))
    return Template("Camera.html", context)
