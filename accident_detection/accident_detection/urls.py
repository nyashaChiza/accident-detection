from accident_detection_api import urls as accident_detection_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('app/', include(accident_detection_urls)),
]
