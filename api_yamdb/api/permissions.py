from rest_framework import permissions


class Admin(permissions.BasePermission):
    """Дать разрешение для ВСЕХ методов или если пользователь
    авторизован и является администратором или суперюзером.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class AdminOrReadOnly(permissions.BasePermission):
    """Дать разрешение для SAFE методов или если пользователь
    авторизован и является администратором или суперюзером.
    """

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))


class AdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    """Дать разрешение для SAFE методов или если пользователь
    авторизован и является администратором,модератором или суперюзером
    ИЛИ автором комментария/ревью.
    """

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin
                or request.user.is_moderator
                or obj.author == request.user)


class ForReviewAndComment(permissions.BasePermission):
    """Дать разрешение для ревью и комментариев: читать могут все, обычный user
    имеет полные права на свои объекты, moderator может править и удалять все
    объекты, администратор и суперюзер - полные права.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user == obj.author
            or request.user.is_moderator and request.method != 'POST'
            or request.user.is_admin
            or request.user.is_superuser
        )
