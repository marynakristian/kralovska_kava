from django.test import TestCase
from menu.models import Reservation

class ReservationModelTest(TestCase):
    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            name="Test User",
            email="test@example.com",
            date="2023-12-31",
            time="12:00:00"
        )
        self.assertEqual(reservation.name, "Test User")
