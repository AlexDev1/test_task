import django_filters
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.catalog.models import Product, FilialPrice, Filial, Characteristics
from apps.catalog.serializers import ProductSerializer, FilialPriceSerializer, FilialSerializer, \
    CharacteristicsSerializer


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['name']


class ProductFilter(django_filters.FilterSet):
    filial = django_filters.NumberFilter(name="filial_id")

    class Meta:
        model = FilialPrice
        fields = ['filial']


class FilialPriceViewSet(viewsets.ViewSet):
    queryset = FilialPrice.objects.all()
    serializer_class = FilialPriceSerializer
    http_method_names = ['get', 'post', ]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter
    lookup_url_kwarg = ('product_id')

    def get_queryset(self):
        queryset = FilialPrice.objects.all()
        filial = self.request.query_params.get('filial', None)
        if filial:
            queryset = queryset.filter(filial_id=filial)
        return queryset

    def list(self, request, **kwargs):
        qs = self.get_queryset()
        serializer = self.serializer_class(data=qs, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(methods=['GET'], detail=True)
    def price(self, *args, **kwargs):
        product_id = kwargs.get('product_id')
        qs = self.get_queryset().filter(product=product_id)
        serializer = FilialPriceSerializer(data=qs, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)

    @action(methods=['GET'], detail=True)
    def characterictic(self, *args, **kwargs):
        product_id = kwargs.get('product_id')
        qs = Characteristics.objects.filter(product=product_id)
        serializer = CharacteristicsSerializer(data=qs, many=True)
        serializer.is_valid()
        return Response(data=serializer.data)


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer


class CharacteristicsViewSet(viewsets.ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = CharacteristicsSerializer
