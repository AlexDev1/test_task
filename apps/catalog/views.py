from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.catalog.models import Product, FilialPrice, Filial, Characteristics
from apps.catalog.serializers import ProductSerializer, FilialPriceSerializer, FilialSerializer, \
    CharacteristicsSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class FilialPriceViewSet(viewsets.ModelViewSet):
    queryset = FilialPrice.objects.all()
    serializer_class = FilialPriceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['filial']


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class CharacteristicsViewSet(viewsets.ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = CharacteristicsSerializer
