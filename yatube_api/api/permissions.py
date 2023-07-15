from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response


class AuthenticatedOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        return obj.author == request.user


class GroupReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            # тест требует выводить этот статус при попытки на создании группы.
            response = {"detail": "Создавать Группу может только админ."}
            return Response(
                response,
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return request.method in permissions.SAFE_METHODS


class AuthenticationOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated
