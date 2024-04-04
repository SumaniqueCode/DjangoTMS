from rest_framework import permissions

class IsTaskManager(permissions.BasePermission):
    """Custom Permissions for the tasks"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        return False