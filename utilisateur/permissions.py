from rest_framework.permissions import BasePermission

class is_superadmin(BasePermission):
    def has_permission(self,request, view):
        return request.user.is_authenticated and request.user.role == 'superadmin'
        

class is_admin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    