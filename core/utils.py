from django.db import models
from django_lifecycle import LifecycleModelMixin
from django.utils import timezone
from django.conf import settings

class Base_content(LifecycleModelMixin,models.Model):
    status_choice = (
        (True,"Active"),
        (False,"Inactive")
    )
    created_on = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True,choices=status_choice,blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
