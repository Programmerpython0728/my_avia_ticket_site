from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from my_avia_kassa.models import Order, Ticket

User = get_user_model()

class OrderAPITestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Ticket yaratish
        self.ticket = Ticket.objects.create(
            name='Test Ticket',
            price=100.00,
            description='This is a test ticket'
        )

        # Order yaratish
        self.order = Order.objects.create(
            product=self.ticket,
            customer=self.user,
            phone_number='+998901234567',
            quantity=2
        )

        # API ga autentifikatsiya qilish
        self.client.force_authenticate(user=self.user)

    def test_create_order(self):

        url = '/api/orders/'
        data = {
            'product': self.ticket.id,
            'customer': self.user.id,
            'phone_number': '+998901234567',
            'quantity': 3,
            'status': 'Sotib olinmadi',
            'is_paid': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
    def test_get_order_list(self):

        url = '/api/orders/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Faqat bitta order mavjud

    def test_get_order_detail(self):

        url = f'/api/orders/{self.order.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone_number'], '+998901234567')

    def test_update_order(self):

        url = f'/api/orders/{self.order.id}/'
        data = {
            'quantity': 5,
            'status': 'Sotib olindi'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.quantity, 5)
        self.assertEqual(self.order.status, 'Sotib olindi')

    def test_delete_order(self):

        url = f'/api/orders/{self.order.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)  # Order o'chirilganligini tekshirish