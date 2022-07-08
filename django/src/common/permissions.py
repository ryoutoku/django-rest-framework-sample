from rest_framework.permissions import BasePermission


class AdminPermission(BasePermission):
    """
    userがadmin権限(is_superuser)である場合に実行できる
    """

    def has_permission(self, request, view):
        return request.user.is_superuser
