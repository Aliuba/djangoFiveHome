from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from .managers import CustomEmployeeManager

class CustomEmployee(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_employee'
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomEmployeeManager()
