from django.db import models
from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from my_avia_kassa.filters import TicketFilters
from my_avia_kassa.models import Ticket
from my_avia_kassa.permissions import IsOwnerOrReadOnly, IsStaffOrReadyOnly
from my_avia_kassa.serializers import TicketSerializers


class CustomPagination(PageNumberPagination):
    page_size = 5


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsStaffOrReadyOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializers
    pagination_class = CustomPagination


