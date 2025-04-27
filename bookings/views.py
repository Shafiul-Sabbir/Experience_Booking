from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.exceptions import PermissionDenied

# This view is used to list and create bookings for experiences
# The customer can only see their own bookings and create new ones
class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # This method is called when retrieving a list of bookings
    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

    # This method is called when creating a new booking by the customer
    def perform_create(self, serializer):
        if self.request.user.role != 'customer':
            raise PermissionDenied("Only customers can create a booking.")

        serializer.save(customer=self.request.user)

# This view is used to retrieve or delete a specific booking
class BookingDeleteView(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # This method is called when retrieving a list of bookings
    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)

    # This method is called when deleting a booking
    def destroy(self, request, *args, **kwargs):
        if request.user.role != 'customer':
            raise PermissionError("Only customers can delete their bookings.")
        return super().destroy(request, *args, **kwargs)

