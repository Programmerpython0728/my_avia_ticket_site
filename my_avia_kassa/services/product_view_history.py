from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from my_avia_kassa.models import ProductViewHistory
from my_avia_kassa.serializers import ProductViewHistorySerializers
from drf_yasg.utils import swagger_auto_schema


class ProductViewHistoryCreate(APIView):
    serializer_class = ProductViewHistorySerializers

    @swagger_auto_schema(request_body=ProductViewHistorySerializers)
    def post(self, request):
        serializer = ProductViewHistorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)