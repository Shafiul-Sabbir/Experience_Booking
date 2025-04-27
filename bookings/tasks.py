from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Booking

# This task will expire pending bookings after 15 minutes.
# It will check if the booking is still pending and if it was created more than 15 minutes ago, then it will change its booking status as 'cancelled'.
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

'''
Celery worker
These Two commands are used to start the Celery worker and beat scheduler. and they should be run in separate terminal windows.
The worker processes the tasks, and the beat scheduler sends periodic tasks to the worker.

commands:
celery -A experience_booking worker --loglevel=info --pool=solo
celery -A experience_booking beat --loglevel=info


'''
