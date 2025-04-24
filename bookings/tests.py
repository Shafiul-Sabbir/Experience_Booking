from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from experiences.models import AvailabilitySlot, Experience
from bookings.models import Booking
from datetime import date
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class BookingAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.customer = User.objects.create_user(username='customer1', password='testpass', role='customer')
        self.guide = User.objects.create_user(username='guide1', password='testpass', role='guide')

        self.experience = Experience.objects.create(
            provider=self.guide,
            title='Test Experience',
            description='A great experience',
            start_date=date(2025, 5, 1),
            end_date=date(2025, 5, 2),
            capacity=5
        )

        self.slot = AvailabilitySlot.objects.create(
            experience=self.experience,
            date=date(2025, 5, 1),
            capacity=2,
            booked_count=0
        )

        self.booking_url = reverse('booking-list-create')

        # JWT Tokens
        self.customer_tokens = get_tokens_for_user(self.customer)
        self.guide_tokens = get_tokens_for_user(self.guide)

        self.customer_auth_header = {
            'HTTP_AUTHORIZATION': f'Bearer {self.customer_tokens["access"]}'
        }
        self.guide_auth_header = {
            'HTTP_AUTHORIZATION': f'Bearer {self.guide_tokens["access"]}'
        }

    def test_customer_can_create_booking(self):
        response = self.client.post(
            self.booking_url,
            {'slot': self.slot.id},
            **self.customer_auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().customer, self.customer)

    def test_guide_cannot_create_booking(self):
        response = self.client.post(
            self.booking_url,
            {'slot': self.slot.id},
            **self.guide_auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Booking.objects.count(), 0)

    def test_customer_can_delete_own_booking(self):
        booking = Booking.objects.create(customer=self.customer, slot=self.slot)
        delete_url = reverse('booking-delete', kwargs={'pk': booking.pk})
        response = self.client.delete(delete_url, **self.customer_auth_header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

    def test_booking_fails_when_slot_full(self):
        self.slot.booked_count = 2
        self.slot.save()
        response = self.client.post(
            self.booking_url,
            {'slot': self.slot.id},
            **self.customer_auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("This slot is fully booked.", str(response.data))
