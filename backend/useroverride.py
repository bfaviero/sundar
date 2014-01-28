from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from backend.models import *

class CustomBackend:
    def authenticate(self, email=None, password=None, username=None):
        if username and not email:
            email=username
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except get_user_model().DoesNotExist:
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