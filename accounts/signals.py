from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import timedelta, date
from django.utils.timezone import now
from audit.models import  *
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from .middleware import get_current_request

@receiver(post_save, sender=LogEntry)
def create_log_entry_extension(sender, instance, created, **kwargs):
    request = get_current_request()
    if created:
        if request:
            ip_address = get_client_ip(request)
        
        LogEntryExtension.objects.create(
            log_entry=instance,
            created_at=now(),
            ip_address=ip_address,
        )

# Helper function to get client IP from request
def get_client_ip(request):
    """
    Retrieve the client's IP address from the request.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
