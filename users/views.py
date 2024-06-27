from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserCreationSerializer, UserSerializer, UserUpdateSerializer


class UserCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "photo": user.photo,
            "bio": user.bio
        })   

class UserUpdateView(generics.UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserUpdateSerializer   
    permission_classes = [AllowAny]