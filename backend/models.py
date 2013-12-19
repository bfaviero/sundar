from django.db import models
from django import forms
from decimal import Decimal

class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase
    def to_python(self, value):
        try:
           return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
           return None
       
class Supplier(models.Model):
    """supplier description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    user_id = models.ForeignKey(models.User, unique=True)
    email_addr = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, widget=forms.PasswordInput)    
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    """supplier items"""
    #image = models.ImageField(upload_to=)
    supplier_id = models.ForeignKey()
    images_json_list = models.TextField(null=True)
    material = models.TextField()#DataFrame of DeviceMotion data
    cost = CurrencyField()
    time_updated = models.DateTimeField(auto_now_add=True)
    time_created = models.DateTimeField(auto_now_add=True)

class Designer(models.Model):
    """designer description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    user_id = models.ForeignKey(models.User, unique=True)
    email_addr = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, widget=forms.PasswordInput)    
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)

 