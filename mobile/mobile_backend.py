from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from templating import Template, error_page

def index(request):
    return Template("index.html")

def render_edit_product(request):
    return Template("edit_product.html")

def render_product_list(request):
    return Template("product_list.html")

def render_sign_up(request):
    return Template("sign_up.html")

def example(request):
    return Template("Example.html")

def camera(request):
    return Template("Camera.html")
