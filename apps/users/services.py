from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class UserService:

    @staticmethod
    def register_user(data):
        serializer = UserRegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return {"message": "User registered successfully"}

    @staticmethod
    def login_user(data):
        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
            "email": user.email
        }
