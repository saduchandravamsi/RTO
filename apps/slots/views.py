from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .services import SlotService


class SlotBookingAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        result = SlotService.book_slot(request.user, request.data)
        return Response(result, status=status.HTTP_201_CREATED)

from .serializers import MyBookingSerializer


class MyBookingsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        slots = SlotService.get_my_bookings(request.user)
        serializer = MyBookingSerializer(slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
