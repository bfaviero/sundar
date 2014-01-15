from django.db import models
from django import forms
from decimal import Decimal
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms
from datetime import datetime
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from datetime import datetime
class CustomBackend:
    #This must be called before login(request, user)
    def authenticate(self, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None
    # Required
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = datetime.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin '
                    'site.')
    is_active = models.BooleanField(default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    last_logged_in = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

class Supplier(CustomUser):
    """Supplier description"""
    company_name = models.CharField(db_index=True, max_length=128, default="", blank=True)

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
    in_stock = models.BooleanField(default=True, blank=True)
    price_on_request = models.BooleanField(default=False, blank=True)
    made_to_order = models.BooleanField(default=False, blank=True)
    lead_time = models.DecimalField(max_digits=19, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=19, decimal_places=2)
    wholesale_price_units = models.CharField(max_length=32, default="", blank=True)
    volume_discount = models.CharField(max_length=32, default="", blank=True)
    fabric_width = models.DecimalField(max_digits=19, decimal_places=5)
    fabric_width_units = models.CharField(max_length=32, default="", blank=True)
    material_type = models.CharField(max_length=32, default="", blank=True)
    fiber_type = models.CharField(max_length=32, default="", blank=True)
    textile_type = models.CharField(max_length=512, default="", blank=True)
    weave_type = models.CharField(max_length=32, default="", blank=True)
    description = models.CharField(max_length=512, default="", blank=True)
    weight = models.CharField(max_length=32, default="", blank=True)
    color = models.CharField(max_length=32, default="", blank=True)
    dyeing = models.CharField(max_length=32, default="", blank=True)
    color_fast_testing = models.CharField(max_length=32, default="", blank=True)
    country_origin = models.CharField(max_length=32, default="", blank=True)
    sustainability = models.CharField(max_length=32, default="", blank=True)
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

