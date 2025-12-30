from django import forms
from .models import *
from django.contrib.auth.password_validation import validate_password, ValidationError as PasswordValidationError
import json
from django.contrib.auth.forms import AuthenticationForm

