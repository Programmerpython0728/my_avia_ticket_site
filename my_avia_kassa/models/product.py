from django.db import models

class Ticket(models.Model):


    flight_number = models.CharField(max_length=50)  # Reys raqami
    departure_city = models.CharField(max_length=100)  # Uchish shahri
    arrival_city = models.CharField(max_length=100)  # Qo'nish shahri
    departure_time = models.DateTimeField()  # Uchish vaqti
    arrival_time = models.DateTimeField()  # Qo'nish vaqti
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narx
    available_seats = models.IntegerField()  # Mavjud o'rindiqlar soni
    airline = models.CharField(max_length=100)  # Havo yo'li kompaniyasi

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} to {self.arrival_city}"
