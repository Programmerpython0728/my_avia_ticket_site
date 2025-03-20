from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from my_avia_kassa.models import Order,Review,Ticket
from my_avia_kassa.permissions import IsOwnerOrReadOnly,IsStaffOrReadyOnly
from my_avia_kassa.serializers import ReviewSerializers,TicketSerializers,OrderSerializers

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


#
#
