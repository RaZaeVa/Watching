from rest_framework import permissions


class IsSuperuserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser


class IsOwnerOrAdminCanChange(permissions.BasePermission):
    """
    Разрешение, которое позволяет только владельцу объекта изменять его,
    а администраторам разрешено изменять все объекты.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or (request.user and request.user.is_superuser)


class IsAuthenticatedOrCreateOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет просматривать объекты всем пользователям,
    но разрешает создание только зарегистрированным пользователям.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_active