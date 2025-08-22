from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer


# Example: List all users (only for authenticated users)
class UserListView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
