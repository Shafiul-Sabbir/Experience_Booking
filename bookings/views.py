from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.exceptions import PermissionDenied

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.role != 'customer':
            raise PermissionDenied("Only customers can create a booking.")

        serializer.save(customer=self.request.user)

class BookingDeleteView(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

    def destroy(self, request, *args, **kwargs):
        if request.user.role != 'customer':
            raise PermissionError("Only customers can delete their bookings.")
        return super().destroy(request, *args, **kwargs)

