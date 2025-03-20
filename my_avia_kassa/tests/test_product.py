
from rest_framework import status,reverse
from rest_framework.test import APITestCase
from my_avia_kassa.models import Ticket
from django.contrib.auth import get_user_model

User = get_user_model()


class TicketViewSetTestCase(APITestCase):
    fixtures = ['products']

    def setUp(self):
        self.user = User.objects.create_user(phone_number='+998931500728', password='testpass')
        self.staff_user = User.objects.create_user(phone_number='+998881550728', password='staffpass', is_staff=True)


        self.product1 = Ticket.objects.create(
            flight_number="AA123",
            departure_city="New York",
            arrival_city="Los Angeles",
            departure_time="2023-10-01T12:00:00Z",
            arrival_time="2023-10-01T17:00:00Z",
            price=299.99,
            available_seats=150,
            airline="American Airlines"
        )
        self.product2 = Ticket.objects.create(
            flight_number="BB456",
            departure_city="Chicago",
            arrival_city="Miami",
            departure_time="2023-10-02T12:00:00Z",
            arrival_time="2023-10-02T15:00:00Z",
            price=199.99,
            available_seats=200,
            airline="Delta Airlines"
        )

    def test_product_list(self):
        url = reverse('product-view-history-create')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_product_detail(self):
        url = reverse('product-view-history-create', args=[self.product1.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['flight_number'], 'AA123')



    def test_permission_denied_for_anonymous_create(self):
        self.client.force_authenticate(user=None)  # "Log out" to make the client anonymous
        url = reverse('product-view-history-create')
        data = {'flight_number': 'CC789',
                'departure_city': 'San Francisco',
                'arrival_city': 'Seattle',
                'departure_time': '2023-10-03T12:00:00Z',
                'arrival_time': '2023-10-03T14:00:00Z',
                'price': 399.99,
                'available_seats': 100,
                'airline': 'United Airlines'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_permission_granted_for_staff(self):
        url = reverse('product-view-history-create')
        self.client.force_authenticate(self.staff_user)
        data = {'flight_number': 'CC789',
                'departure_city': 'San Francisco',
                'arrival_city': 'Seattle',
                'departure_time': '2023-10-03T12:00:00Z',
                'arrival_time': '2023-10-03T14:00:00Z',
                'price': 399.99,
                'available_seats': 100,
                'airline': 'United Airlines'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)