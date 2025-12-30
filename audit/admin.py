from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.admin.models import LogEntry
from .models import *
# Register your models here.

class LogEntryAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
admin.site.register(LogEntry,LogEntryAdmin)
    
class LogEntryExtensionAdmin(admin.ModelAdmin):
    list_display = ('id', 'log_entry', 'created_at', 'ip_address', 'custom_button')

    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('log_entry')
    
    # Custom button for 'UserAnswer'
    def custom_button(self, obj):
        log_entry_admin_url = reverse('admin:admin_logentry_change', args=[obj.log_entry.id])
        return format_html(
            '<a class="button" href="{}">View Log Details</a>',
            log_entry_admin_url
        )
    custom_button.short_description = 'View Log Entry'
   
admin.site.register(LogEntryExtension,LogEntryExtensionAdmin) 