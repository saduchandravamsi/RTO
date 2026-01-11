from django.urls import path
from .views import UserRegisterAPI, UserLoginAPI

urlpatterns = [
    path('register/', UserRegisterAPI.as_view()),
    path('login/', UserLoginAPI.as_view()),
]
