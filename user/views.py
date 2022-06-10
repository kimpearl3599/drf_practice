from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissons


class MyPermisson(permissons.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_rank)
        return


class UserApiView(APIView):
    permisson_classes = [MyPermisson]

    def get(self, request):
        return Response({"message": "get!"})

    def post(self, request):
        return Response({"message": "post!"})

    def delete(self, request):
        return Response({"message": "delete!"})

    def put(self, request):
        return Response({"message": "put!"})
