from .models import Path, RolePathPermission


def has_permission(user, path_name, action):
    """
    path_name: "User List"
    action: can_view | can_add | can_edit | can_delete
    """

    if not user.is_authenticated:
        return False

    if not user.role:
        return False

    try:
        path = Path.objects.get(
            path_name=path_name,
            status="Active"
        )

        permission = RolePathPermission.objects.get(
            role=user.role,
            path=path
        )

    except (Path.DoesNotExist, RolePathPermission.DoesNotExist):
        return False

    return getattr(permission, action, False)
