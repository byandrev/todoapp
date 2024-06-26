from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserCreationSerializer, UserSerializer


class UserCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]