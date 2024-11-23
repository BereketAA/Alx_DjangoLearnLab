from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admins to edit objects.
    """

    def has_permission(self, request, view):
        # Safe methods are GET, HEAD, and OPTIONS
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user.is_staff