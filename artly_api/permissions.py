from rest_framework import permissions

# This code was appropriated from Code Institute's DRF_API walkthrough project
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user