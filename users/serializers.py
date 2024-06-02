from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserCreationSerializer, self).create(validated_data)
        
