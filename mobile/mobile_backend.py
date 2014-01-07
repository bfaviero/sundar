from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from backend.models import Supplier, Item
from backend.item_api import get_items
from django.forms.models import model_to_dict
from constants import TEXTILE_TYPES, WEAVE_TYPES, WHOLESALE_PRICE_UNITS,\
    FABRIC_WITDH_UNITS, BASIC_MATERIAL_TYPES, FABRIC_WEIGHT_UNITS, FIBER_TYPES

from django.contrib.auth.signals import user_logged_in, user_logged_out


def render_login(request):
    context = {}
    context.update(csrf(request))
    return Template("login.html", context)

def login(request):
    email_addr = request_arg(request, "email_addr")
    password = request_arg(request, "password")
    if email_addr == check_password(password):
        pass
    return Template("login.html")

def sign_up(request):
    c_name = request_arg(request, "company_name")
    email_addr = request_arg(request, "email_addr")
    password = request_arg(request, "password")
    if is_password_usable(password):
        db_pass = make_password(password)
        Supplier(c_name, email_addr, db_pass)

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
               "fiber_types": FIBER_TYPES}
    context.update(csrf(request))
    return Template("edit_product.html", context)

def render_product_list(request):
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
