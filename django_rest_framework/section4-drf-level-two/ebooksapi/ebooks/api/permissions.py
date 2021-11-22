from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """
    해당 유저가 admin이면 CRUD 허용해주고,
    request.method가 ('GET', 'HEAD', 'OPTIONS') 중 하나이면 READ를 허용해줌.
    """
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin