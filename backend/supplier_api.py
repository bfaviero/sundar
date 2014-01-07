from templating import Template, error_page
from utils import request_arg, optional_request_arg
from django.http import HttpResponse
from django.core.context_processors import csrf
from utils import request_arg, optional_request_arg as ora, optional_string_request_arg as osra
from django.shortcuts import redirect
from models import Supplier, Item
from datetime import datetime
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.hashers import make_password, check_password, is_password_usable


def create_supplier(request):
    password = request_arg(request, "password")
    if password != "" and password == request_arg(request, "confirm_password"):
        password_candidate = make_password(password)
        if not is_password_usable(password_candidate):
            return HttpResponse("Password cannot be empty.")
        else: 
            new_supp = Supplier()
            new_supp.password = password_candidate
            new_supp.email_addr = request_arg(request, "email_addr")
            new_supp.company_name = request_arg(request, "company_name")
            new_supp.save()
            user_logged_in.send(sender=Supplier,request=request,user=new_supp)
            return redirect("/mobile/product_list")
    return HttpResponse("Error: Passwords do not match.")

@user_logged_in
def update_supplier(request):
    return HttpResponse("SUCCESS update_supplier ")

@user_logged_in
def delete_supplier(request):
    return HttpResponse("SUCCESS delete_supplier ")

def login_supplier(request):
    email_addr = request_arg(request, "email_addr")
    password = request_arg(request, "password")
    user = Supplier.objects.get(email_addr=email_addr)
    if user.password == check_password(password):
        user_logged_in.send(sender=Supplier,request=request,user=user)
        return redirect("/mobile/product_list")
    return redirect("/mobile/sign_up")
