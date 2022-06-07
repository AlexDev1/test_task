from rest_framework import serializers

from apps.catalog.models import Product, Filial, Characteristics, FilialPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', ]


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ['id', 'name', 'region']


class CharacteristicsSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = Characteristics
        fields = ['self', 'name', 'product']


class FilialPriceSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(many=True)

    class Meta:
        model = FilialPrice
        fields = ['id', 'product', 'filial', 'price']
