from my_avia_kassa.models.order import Order
from django.db import models
class Payment(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payments')
    stripe_charge_id=models.CharField(max_length=20)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    
