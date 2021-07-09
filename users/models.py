from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from core.utils import upload_image_path


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
        if not username:
            raise ValueError(_('User must have an username'))
        if not email:
            raise ValueError(_('User must have an email address'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **kwargs)


class User(PermissionsMixin, AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    email = models.EmailField(_('Email Address'), unique=True)
    username = models.CharField(_('Username'), max_length=100, unique=True, validators=[username_validator])
    first_name = models.CharField(_('First Name'), max_length=254, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=254, blank=True)
    bio = models.TextField(_('Bio'), blank=True)
    url = models.URLField(_('URL'), blank=True)
    profile_photo = models.ImageField(_('Profile Photo'), upload_to=upload_image_path, blank=True)
    is_verified = models.BooleanField(_('Verified'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Superuser'), default=False)
    last_login = models.DateTimeField(_('Last Login'), blank=True, null=True)
    date_joined = models.DateTimeField(_('Date Joined'), blank=True, auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username

    @property
    def display_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.username}'
    
    def email_user(self, subject, message):
        return send_mail(subject, message, recipient_list=[self.email], fail_silently=False)