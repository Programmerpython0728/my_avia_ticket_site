from django.core.exceptions import ValidationError
from my_avia_kassa.models import Order

def place_order(product,customer,quantity):
    if product and customer and quantity >0:
        order=Order(product=product,customer=customer,quantity=quantity)
        order.save()
        return order
    else:
        raise ValidationError("Xarid ma'lumotlarida xatolik bor qayta tekshirib ko'ring")
    
