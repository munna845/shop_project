from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    owner_allowed_actions = ['retrieve', 'update', 'partial_update', 'destroy']

    
    def has_object_permission(self, request, view, obj):
        #admins alwys allowed
        if request.user.is_staff:
            return True

        # Owners allowed certain actions only
        if obj.user == request.user:
            if view.action in self.owner_allowed_actions:
                return True

        return False