from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
