from rest_framework.serializers import ModelSerializer

from testAPI_v2.models import ProductSet, Recipient, Order


class ProductSetSerializer(ModelSerializer):
    class Meta:
        model = ProductSet
        fields = '__all__'


class RecipientSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class RecipientFIOSerializer(ModelSerializer):
    class Meta:
        model = Recipient
        fields = ['surname',
                  'name',
                  'patronymic'
                  ]


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderAddressSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['delivery_address']


class OrderStatusSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
