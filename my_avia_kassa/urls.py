from . import signals
from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .view.misc import *
from .services.product_view_history import ProductViewHistoryCreate
from .services.flashe_sale import FlashSaleListCreateView, check_flash_sale
from my_avia_kassa.view.product import *

router=DefaultRouter()

router.register(r'tickets',TicketViewSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'orders',OrderViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('sale/', FlashSaleListCreateView.as_view(), name='sale'),
     path('check-sale/<int:product_id>/', check_flash_sale, name='product-view-history-create'),
   path('product-view/', ProductViewHistoryCreate.as_view(), name='product-view-history-create'),


]
