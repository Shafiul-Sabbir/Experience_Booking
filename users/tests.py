from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

# this test case will test the user registration API endpoint and check if the user is created successfully with the correct data.
class UserAuthTests(APITestCase):
    def test_user_registration(self):
        data = {
            "username" : "shuvo",
            "email" : "shuvoda@gmail.com",
            "password" : "1234",
            "role" : "customer",
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
