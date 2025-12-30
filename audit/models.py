from django.db import models
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.timezone import now

# Create your models here.
class LogEntryExtension(models.Model):
    log_entry = models.OneToOneField(LogEntry, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"LogEntryExtension for LogEntry {self.log_entry.id}"
    
    class Meta:
        verbose_name = "Log Entry"
        verbose_name_plural = "Log Entries"
        