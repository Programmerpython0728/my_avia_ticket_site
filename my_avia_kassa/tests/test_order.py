from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from my_avia_kassa.models import Order, Ticket

User = get_user_model()

class OrderAPITestCase(APITestCase):
    fixtures = ['order']
    def setUp(self):
        # Foydalanuvchi yaratish, telefon raqami bilan
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            phone_number='+998901234567'  # Telefon raqami qo'shildi
        )

        # Ticket yaratish
        self.ticket = Ticket.objects.create(
            flight_number='1234AB',
            departure_city='Tashkent',
            arrival_city='London',
            departure_time='2025-05-01 15:00:00',
            arrival_time='2025-05-01 17:00:00',
            price=200.00,
            available_seats=50,
            airline='Uzbekistan Airways'
        )

        # Order yaratish
        self.order = Order.objects.create(
            product=self.ticket,
            customer=self.user,
            phone_number='+998901234567',  # Telefon raqami qo'shildi
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
            'status': 'Sotib olinmadi',  # 'status' bo'yicha to'g'ri variant
            'is_paid': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)  # Yangi order yaratish

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
            'status': 'Sotib olindi'  # 'status'ni yangilash
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