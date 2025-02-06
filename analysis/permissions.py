from rest_framework.permissions import (
    BasePermission,
)

class DigitalStatisticsPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False 
        return request.user.has_perm('analysis.can_view_digital_statistics')