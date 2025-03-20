from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from my_avia_kassa.models import Order,Ticket

class OrderSerializers(serializers.ModelSerializer):
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields= ['id', 'product', 'customer', 'quantity', 'created_at', 'total_price', 'phone_number', 'is_paid']

        def __init__(self):
            self.initial_data = None

        def get_total_price(self,obj):
            return obj.product.price * obj.quantity

        def validate_quantity(self,value):
            try:
                product_id=self.initial_data['product']
                product=Ticket.objects.get(id=product_id)
                if value>product.available_seats :
                    raise serializers.ValidationError("Belitlar soni yetarli emas! ")
                if value<1:
                    raise serializers.ValidationError("Xarid qilinayotgan belitlar soni eng kamida 1 ta bo'lishi kerak!")
                return value

            except ObjectDoesNotExist:
                raise serializers.ValidationError("Ticket does not exist!")

        def create(self, validated_data):
            order = Order.objects.create(**validated_data)
            product = order.product
            product.available_seats  -= order.quantity
            product.save()
            self.send_confirmation_email(order)
            return order

        def send_confirmation_email(self, order):
            print(f"Sent confirmation email for Order {order.id}")


