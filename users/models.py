from django.contrib.auth.models import AbstractUser
from django.db import models

# Role based user model
# This model extends the default Django user model to include a role field.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('provider', 'Provider'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"