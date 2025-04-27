from celery import shared_task
from .models import Experience, AvailabilitySlot
from datetime import timedelta

# This task will generate availability slots for an experience.
# It will create slots for each day between the start and end date of the experience.
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


'''
Celery worker
These Two commands are used to start the Celery worker and beat scheduler. and they should be run in separate terminal windows.
The worker processes the tasks, and the beat scheduler sends periodic tasks to the worker.

commands:
celery -A experience_booking worker --loglevel=info --pool=solo
celery -A experience_booking beat --loglevel=info


'''
