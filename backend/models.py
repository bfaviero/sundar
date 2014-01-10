from django.db import models
from django import forms
from decimal import Decimal
from django.contrib.auth.models import User, AbstractBaseUser
from django import forms
from datetime import datetime

class CustomBackend:
    #This must be called before login(request, user) 
    def authenticate(self, email_addr=None, password=None):
        try:
            user = CustomUser.objects.get(email_addr=email_addr)
            if password == user.password:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
    # Required
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class CustomUser(AbstractBaseUser):
    """base User model"""
    """inherited fields: id, password, last_login"""
    email_addr = models.EmailField(max_length=30, unique=True, db_index=True)
    time_created = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email_addr'
  
class Supplier(CustomUser):
    """Supplier description"""
    company_name = models.CharField(db_index=True, max_length=128, default="", blank=True)
    is_staff = models.BooleanField(default=False)
    CustomUser.REQUIRED_FIELDS += ['company_name']

class Designer(CustomUser):
    """Designer description"""
    pass

class Item(models.Model):
    """supplier items"""
    supplier = models.ForeignKey(Supplier)
    image1_url = models.CharField(max_length=255, default="", blank=True)
    image2_url = models.CharField(max_length=255, default="", blank=True)
    image3_url = models.CharField(max_length=255, default="", blank=True)
    image4_url = models.CharField(max_length=255, default="", blank=True)
    image5_url = models.CharField(max_length=255, default="", blank=True)
    product_name = models.CharField(max_length=128, default="", blank=True)
    product_code = models.CharField(max_length=128, default="", blank=True)
    in_stock = models.BooleanField(default="", blank=True)
    lead_time = models.CharField(max_length=32, default="", blank=True)
    wholesale_price = models.CharField(max_length=32, default="", blank=True)
    wholesale_price_units = models.CharField(max_length=32, default="", blank=True)
    volume_discount = models.CharField(max_length=32, default="", blank=True)
    fabric_width = models.CharField(max_length=32, default="", blank=True)
    fabric_width_units = models.CharField(max_length=32, default="", blank=True)
    material_type = models.CharField(max_length=32, default="", blank=True)
    fiber_type = models.CharField(max_length=32, default="", blank=True)
    textile_type = models.CharField(max_length=512, default="", blank=True)
    weave_type = models.CharField(max_length=32, default="", blank=True)
    description = models.CharField(max_length=512, default="", blank=True)
    weight = models.CharField(max_length=32, default="", blank=True)
    color = models.CharField(max_length=32, default="", blank=True)
    dying = models.CharField(max_length=32, default="", blank=True)
    color_fast_testing = models.CharField(max_length=32, default="", blank=True)
    country_origin = models.CharField(max_length=32, default="", blank=True)
    sustainability = models.CharField(max_length=32, default="", blank=True)
    cost = models.CharField(max_length=32, default="", blank=True)
    time_updated = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)


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

