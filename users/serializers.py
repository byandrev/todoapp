from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.password_validation import get_password_validators
from django.conf import settings

from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

    def validate_password(self, value):
        password_validators = get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
        validate_password(
            value, user=self.instance, password_validators=password_validators
        )
        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserCreationSerializer, self).create(validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "photo", "bio", "last_login")
    
