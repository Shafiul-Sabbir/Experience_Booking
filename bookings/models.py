from django.db import models
from django.conf import settings
from experiences.models import AvailabilitySlot

# This model represents a booking made by a customer for an experience slot.
# It contains a foreign key to the user who made the booking and a foreign key to the availability slot booked.
class Booking(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    slot = models.ForeignKey(AvailabilitySlot, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, default='pending')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.slot} ({self.status})"