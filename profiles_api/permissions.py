from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):
    """Allow user toedit therir own profile"""
    def has_object_permissions(self, request, veiw, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user_id
