from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import UserManager 
from core.utils import Base_content
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import date
from django.utils import timezone
from datetime import timedelta
import random
import string
from django.core.exceptions import ValidationError
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.timezone import now
import uuid
from django.contrib.auth.models import Group
# Create your models here.


class Path(models.Model):
    path_name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        default="Active",
        choices=(('Active','Active'), ('Inactive','Inactive'))
    )
    parent = models.ForeignKey('Path', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path_name


class Admin_role(models.Model):
    role_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Path, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role_name
    
    
class RolePathPermission(models.Model):
    role = models.ForeignKey(Admin_role, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    can_add = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)


    
class User(AbstractUser):
    email = models.EmailField(verbose_name = 'email', unique=True)
    created = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    role = models.ForeignKey(Admin_role, on_delete=models.SET_NULL, null=True, blank=True)
    objects = UserManager()


class Team(models.Model):
    name = models.CharField(max_length=100)