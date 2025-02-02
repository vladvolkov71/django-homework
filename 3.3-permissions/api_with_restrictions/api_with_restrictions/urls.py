from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advertisements.views import AdvertisementViewSet

router = DefaultRouter()
# TODO: подключите `AdvertisementViewSet`
router.register('advertisements', AdvertisementViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
] + router.urls
