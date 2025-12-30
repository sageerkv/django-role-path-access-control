from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.admin.models import LogEntry
from .forms import *
from django.urls import path
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q 
import csv
from django.http import HttpResponse, JsonResponse
from datetime import date, datetime
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.forms import DateInput

# Register your models here.


class MyAdminSite(admin.AdminSite):
    """Custom Django Admin Site with Calendar Page"""
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
        ]
        return custom_urls + urls
            
admin.site=MyAdminSite()


class PathAdmin(admin.ModelAdmin):
    list_display = ("id", "path_name", "status", "parent", "created_at")
    search_fields = ("path_name",)
    list_filter = ("status",)
    ordering = ("path_name",)

admin.site.register(Path,PathAdmin)

class AdminRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name", "status", "date")
    search_fields = ("role_name",)
    list_filter = ("status",)

admin.site.register(Admin_role,AdminRoleAdmin)

class RolePathPermissionAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "path",
        "can_view",
        "can_add",
        "can_edit",
        "can_delete",
    )

    list_filter = ("role", "path")
    search_fields = ("role__role_name", "path__path_name")

admin.site.register(RolePathPermission,RolePathPermissionAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin', 'role', 'created')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password', 'is_admin', 'role')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            )
        }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_admin', 'role'),
        }),
    )

    ordering = ('username',)

    def has_delete_permission(self, request, obj=None):
        return False


    
admin.site.register(User,CustomUserAdmin)

