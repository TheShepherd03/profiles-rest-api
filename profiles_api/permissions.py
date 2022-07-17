from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow a user to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """check if user is editing their own profile"""
        if(request.method in permissions.SAFE_METHODS):
            return True

        return obj.id==request.user.id#checks if user attempting to edit is the correct user