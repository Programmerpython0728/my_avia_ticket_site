from django.db import models
from rest_framework import serializers
from my_avia_kassa.models import Ticket,ProductViewHistory,Review,FlashSale

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields="__all__"
class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class ProductViewHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductViewHistory
        fields="__all__"
class FlashSaleSerializers(serializers.ModelSerializer):
    class Meta :
        model=FlashSale
        fields="__all__"
