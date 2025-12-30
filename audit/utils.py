from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType


def log_action(user, action_flag, obj, message):
    LogEntry.objects.log_action(
        user_id=user.id,
        content_type_id=ContentType.objects.get_for_model(obj).id,
        object_id=obj.id,
        object_repr=str(obj),
        action_flag=action_flag,
        change_message=message,
    )
