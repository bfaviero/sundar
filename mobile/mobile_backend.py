from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from backend.models import Supplier

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
    context = {}
    context.update(csrf(request))
    return Template("edit_product.html", context)

def render_product_list(request):
    context = {}
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
