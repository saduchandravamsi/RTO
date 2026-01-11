from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data['username'],
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        data['user'] = user
        return data


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    mobile_number = serializers.CharField()
    photo = serializers.ImageField()

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )

        UserProfile.objects.create(
            user=user,
            mobile_number=validated_data['mobile_number'],
            photo=validated_data['photo']
        )

        return user
