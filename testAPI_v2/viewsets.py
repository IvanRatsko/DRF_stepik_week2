from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from testAPI_v2.models import ProductSet, Recipient, Order
from testAPI_v2.serializers import ProductSetSerializer, RecipientSerializer, RecipientFIOSerializer, \
    OrderSerializer, OrderAddressSerializer, OrderStatusSerializer


class ProductSetViewSet(ReadOnlyModelViewSet):
    queryset = ProductSet.objects.all()
    serializer_class = ProductSetSerializer


class RecipientViewSet(ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    http_method_names = ['get', 'post', 'patch']

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['patch'])
    def change_fio(self, request, pk=None):
        recipient_fio = self.get_object()
        serializer = RecipientFIOSerializer(recipient_fio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'patch']

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['order_created_datetime', 'status']
    search_fields = ['order_created_datetime', 'status']

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['patch'])
    def change_delivery_address(self, request, pk=None):
        delivery_address = self.get_object()
        serializer = OrderAddressSerializer(delivery_address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def change_order_status(self, request, pk=None):
        order_status = self.get_object()
        serializer = OrderStatusSerializer(order_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
