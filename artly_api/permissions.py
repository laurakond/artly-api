from rest_framework import permissions


# This code was appropriated from Code Institute's DRF_API walkthrough project
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Checks if the user is the owner of the artwork, if not, only gives
    Read-only access.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsSellerOrReadOnly(permissions.BasePermission):
    """
    Checks if the user is the seller of the artwork, if not, only gives
    Read-only access.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.seller == request.user
