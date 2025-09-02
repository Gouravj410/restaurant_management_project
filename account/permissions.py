from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsManagerOrAdminOrReadOnly(BasePermission):
    message = "Permission Denied"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.role in ["Manager", "Admin"]

class IsWaiterOnly(BasePermission):
    message = "Permission Denied"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.role == "Waiter"

class IsCashierOnly(BasePermission):
    message = "Permission Denied"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated
        return request.user.is_authenticated and request.user.role == "Cashier"
