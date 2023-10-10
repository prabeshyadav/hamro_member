from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account import commons

# Create your models here.



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_verified=models.BooleanField(default=True)
    otp=models.CharField(max_length=200,null=True,blank=True)
    is_verified=models.BooleanField(default=True)
    organization_name = models.CharField(max_length=255,null=True,blank=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    subdomain = models.CharField(max_length=50, null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['organization_name','first_name','last_name','phone_number','subdomain']
    role = models.CharField(max_length=20, choices=commons.USER_ROLES)

    def __str__(self):
        return self.email

