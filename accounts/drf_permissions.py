from rest_framework.permissions import BasePermission
from .permissions import has_permission


class HasAccessPermission(BasePermission):

    def has_permission(self, request, view):
        required = getattr(view, 'required_permission', None)

        if not required:
            return True

        try:
            path_name, action = [x.strip() for x in required.split(',', 1)]
        except ValueError:
            return False

        action_map = {
            'view': 'can_view',
            'add': 'can_add',
            'edit': 'can_edit',
            'delete': 'can_delete',
        }

        if action not in action_map:
            return False

        return has_permission(
            user=request.user,
            path_name=path_name,
            action=action_map[action]
        )
