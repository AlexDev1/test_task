from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.routers import DefaultRouter
from api.schemes import BothHttpAndHttpsSchemaGenerator
from apps.catalog.views import CatalogViewSet, FilialPriceViewSet, FilialViewSet, CharacteristicsViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'product', CatalogViewSet, basename='product')
router.register(r'catalog', FilialPriceViewSet, basename='catalog')
router.register(r'filial', FilialViewSet, basename='filial')
router.register(r'characteristics', CharacteristicsViewSet, basename='characteristics')


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="Api ",
        license=openapi.License(name="License"),
    ),
    public=False,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    authentication_classes=[SessionAuthentication, BasicAuthentication],
    permission_classes=[permissions.AllowAny],
)
api_urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
app_name = 'api-root'

api_urlpatterns += router.urls
