from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """admin - CRUD / other - Read only"""
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin