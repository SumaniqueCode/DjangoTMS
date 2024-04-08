from rest_framework import permissions

class IsTaskListManagerOrNot(permissions.BasePermission):
    """Custom Permisions for TaskLists"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile == obj.created_by
class IsTaskManagerOrNot(permissions.BasePermission):
    """Custom Permissions for the tasks"""
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user.profile.house != None
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile.house == obj.task_list.house
    
class IsAttachmentManagerOrNor(permissions.BasePermission):
    """Custom permissions for attachments"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True   
        if not request.method.is_anonymous:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.profile.house == obj.task.task_list.house