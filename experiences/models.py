from django.db import models
from django.conf import settings

class Experience(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE )
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.title

class AvailabilitySlot(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='slots')
    date = models.DateField()
    capacity = models.IntegerField()
    booked_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.experience.title} - {self.date}"