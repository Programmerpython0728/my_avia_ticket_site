from django.db import models
from bilding.models import Payment
from rest_framework import serializers

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__aLL__"
