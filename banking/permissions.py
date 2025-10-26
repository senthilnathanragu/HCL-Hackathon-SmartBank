from rest_framework import permissions

# Only allow users with role 'customer'
class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'customer')

# Only allow users with role 'admin'
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')

# Only allow users with role 'auditor'
class IsAuditor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'auditor')