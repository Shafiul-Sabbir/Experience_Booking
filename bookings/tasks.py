from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Booking

@shared_task
def expire_pending_bookings():
    expiration_time = timezone.now() - timedelta(minutes=15)  # 15 minutes expiration time
    expired = Booking.objects.filter(status="pending", booked_at__lt=expiration_time)
    for booking in expired:
        slot = booking.slot
        if slot.booked_count > 0:
            slot.booked_count -= 1
            slot.save()
        booking.status = "cancelled"
        booking.save()

# Celery worker
# celery -A experience_booking worker --loglevel=info --pool=solo
# celery -A experience_booking beat --loglevel=info --pool=solo
