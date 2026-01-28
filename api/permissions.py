from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow anyone to see the post (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow the author to change it (PUT, DELETE)
        return obj.author == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows read-only access to anyone, 
    but only admins can POST, PUT, PATCH, or DELETE.
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only allow write access to staff users
        return bool(request.user and request.user.is_staff)