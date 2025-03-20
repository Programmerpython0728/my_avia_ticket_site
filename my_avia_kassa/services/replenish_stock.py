from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from my_avia_kassa.models import Ticket
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@api_view(['POST'])
@swagger_auto_schema(operation_description="Admin replenishes stock for a product")
@staff_member_required
def admin_replenish_stock(request, product_id, amount):
    try:
        # amount = int(request.POST.get('amount', 0))
        product = Ticket.objects.get(id=product_id)
        product.increase_stock(amount)

        return JsonResponse({'status': 'success', 'message': f'Successfully replenished stock by {amount}'})

    except Ticket.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product does not exist'}, status=400)

    except ValueError:
        return HttpResponseBadRequest('Invalid input.')