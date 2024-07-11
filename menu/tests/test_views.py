from django.test import TestCase, Client
from django.urls import reverse
from menu.models import Reservation

class ReservationViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.reservation_url = reverse('reservations')

    def test_get_reservation_page(self):
        response = self.client.get(self.reservation_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_app/reservations.html')

    def test_post_reservation(self):
        data = {
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'phone': '987654321',
            'date': '2024-07-12',
            'time': '19:00:00',
            'number_of_people': 2
        }
        response = self.client.post(self.reservation_url, data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Reservation.objects.count(), 1)
        reservation = Reservation.objects.first()
        self.assertEqual(reservation.name, 'Jane Doe')
