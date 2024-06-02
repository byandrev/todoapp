from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from .serializers import UserCreationSerializer

class UserCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]