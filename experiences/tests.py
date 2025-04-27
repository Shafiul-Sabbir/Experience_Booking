from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from .models import Experience

# Test case for provider user authentication and experience creation
class ExperienceTests(APITestCase):
    # Set up the test case with a provider user
    def setUp(self):
        self.provider = User.objects.create_user(
            username='provider1',
            password='1234',
            role='provider',
        )
        self.client.force_authenticate(user=self.provider)

    # Test case for creating an experience
    def test_create_experience(self):
        data = {
            "title": "Sundarban Trip",
            "description": "Forest adventure",
            "start_date": "2025-04-25",
            "end_date": "2025-04-26",
            "capacity": 5
        }
        response = self.client.post(reverse('experience-list-create'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 1)