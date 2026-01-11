from django.urls import path
from .views import SlotBookingAPI, MyBookingsAPI

urlpatterns = [
    path('book/', SlotBookingAPI.as_view()),
    path('my/', MyBookingsAPI.as_view()),
]
