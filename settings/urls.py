from django.contrib import admin
from django.urls import path, include

from api.api_url import api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
]
