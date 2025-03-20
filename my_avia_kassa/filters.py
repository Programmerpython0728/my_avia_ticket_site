from django_filters import rest_framework as django_filters
from .models import Ticket

class TicketFilters(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price=django_filters.NumberFilter(field_name='price',lookup_expr='lte')

    class Meta:
        model=Ticket
        fields=['airline','departure_city','arrival_city','min_price','max_price']

