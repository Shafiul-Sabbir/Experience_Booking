from celery import shared_task
from .models import Experience, AvailabilitySlot
from datetime import timedelta

@shared_task
def generate_slots(experience_id):
    try:
        experience = Experience.objects.get(id=experience_id)
        current_date = experience.start_date
        while current_date <= experience.end_date:
            AvailabilitySlot.objects.create(
                experience=experience,
                date=current_date,
                capacity=experience.capacity,
            )
            current_date += timedelta(days=1)
    except Experience.DoesNotExist:
        pass

# Celery worker
# celery -A experience_booking worker --loglevel=info --pool=solo
# celery -A experience_booking beat --loglevel=info --pool=solo

