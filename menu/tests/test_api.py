from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from menu.models import Reservation

class ReservationAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.reservation_url = reverse('reservation-list-create')
        self.reservation_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'date': '2024-07-10',
            'time': '18:30:00'
        }
        self.reservation = Reservation.objects.create(**self.reservation_data)
        self.detail_url = reverse('reservation-detail', args=[self.reservation.id])

    def test_create_reservation(self):
        response = self.client.post(self.reservation_url, self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reservation_list(self):
        response = self.client.get(self.reservation_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reservation_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_reservation(self):
        updated_data = self.reservation_data.copy()
        updated_data['name'] = 'Jane Doe'
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reservation(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
