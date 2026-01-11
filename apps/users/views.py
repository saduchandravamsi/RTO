from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UserService


class UserRegisterAPI(APIView):

    def post(self, request):
        result = UserService.register_user(request.data)
        return Response(result, status=status.HTTP_201_CREATED)

class UserLoginAPI(APIView):

    def post(self, request):
        result = UserService.login_user(request.data)
        return Response(result, status=status.HTTP_200_OK)
