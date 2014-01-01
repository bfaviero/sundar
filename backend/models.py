from django.db import models
from django import forms
from decimal import Decimal
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class Supplier(models.Model):
    """supplier description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
    email_addr = models.EmailField(max_length=255)
    password = models.CharField(max_length=512)    
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(db_index=True, max_length=128, default="", blank=True)

class Item(models.Model):
    """supplier items"""
    #image = models.ImageField(upload_to=)
    supplier = models.ForeignKey(Supplier)
    image1_url = models.CharField(max_length=64, default="", blank=True)
    image2_url = models.CharField(max_length=64, default="", blank=True)
    image3_url = models.CharField(max_length=64, default="", blank=True)
    image4_url = models.CharField(max_length=64, default="", blank=True)
    image5_url = models.CharField(max_length=64, default="", blank=True)
    product_name = models.CharField(max_length=64, default="", blank=True)
    product_code = models.CharField(max_length=64, default="", blank=True)
    inventory = models.CharField(max_length=32, default="", blank=True)
    lead_time = models.CharField(max_length=32, default="", blank=True)
    wholesale_price = models.CharField(max_length=32, default="", blank=True)
    volume_discount = models.CharField(max_length=32, default="", blank=True)
    fabric_width = models.CharField(max_length=32, default="", blank=True)
    material_type = models.CharField(max_length=32, default="", blank=True)
    fiber_type = models.CharField(max_length=32, default="", blank=True)
    textile_types = models.CharField(max_length=512, default="", blank=True)
    weave_type = models.CharField(max_length=32, default="", blank=True)
    description = models.CharField(max_length=512, default="", blank=True)
    weight = models.CharField(max_length=32, default="", blank=True)
    color = models.CharField(max_length=32, default="", blank=True)
    dying = models.CharField(max_length=32, default="", blank=True)
    color_fast_testing = models.CharField(max_length=32, default="", blank=True)
    country_origin = models.CharField(max_length=32, default="", blank=True)
    sustainability = models.CharField(max_length=32, default="", blank=True)
    cost = models.CharField(max_length=32, default="", blank=True)
    time_updated = models.DateTimeField(auto_now_add=True)
    time_created = models.DateTimeField(auto_now_add=True)

class Designer(models.Model):
    """designer description"""
    #profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
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

