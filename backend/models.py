from django.db import models
from django import forms
from decimal import Decimal
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class Supplier(models.Model):
    """supplier description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    user_id = models.CharField(max_length=512)
    email_addr = models.EmailField(max_length=255)
    password = models.CharField(max_length=512)    
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(db_index=True, max_length=128, default="", blank=True)

class Item(models.Model):
    """supplier items"""
    #image = models.ImageField(upload_to=)
    supplier_id = models.CharField(max_length=512)
    images_json_list = models.TextField(null=True)
    product_name = models.CharField(max_length=64)
    product_code = models.CharField(max_length=64)
    inventory = models.CharField(max_length=32)
    lead_time = models.CharField(max_length=32)
    wholesale_price = models.CharField(max_length=32)
    volume_discount = models.CharField(max_length=32)
    fabric_width = models.CharField(max_length=32)
    material_type = models.CharField(max_length=32)
    fiber_type = models.CharField(max_length=32)
    textile_types = models.TextField()
    weave_type = models.CharField(max_length=32)
    description = models.TextField()
    weight = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    dying = models.CharField(max_length=32)
    color_fast_testing = models.CharField(max_length=32)
    country_origin = models.CharField(max_length=32)
    sustainability = models.CharField(max_length=32)
    cost = models.CharField(max_length=32)
    time_updated = models.DateTimeField(auto_now_add=True)
    time_created = models.DateTimeField(auto_now_add=True)

class Designer(models.Model):
    """designer description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    user_id = models.CharField(max_length=512)
    email_addr = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)    
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)


class PhotoUrl(models.Model):
    url = models.CharField(max_length=255)
    uploaded = models.DateTimeField()

    def save(self):                                                                             
        self.uploaded = datetime.now()
        models.Model.save(self)


#class CurrencyField(models.DecimalField):
#    __metaclass__ = models.SubfieldBase
#    def to_python(self, value):
#        try:
#           return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
#        except AttributeError:
#           return None

