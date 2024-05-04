from rest_framework import request
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permis import IsOwner
from advertisements import filters
from advertisements.models import AdvertisementStatusChoices


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = AdvertisementSerializer
    filterset_class = filters.AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.method == "GET":
            return []
        if User.is_superuser:
            return [IsAuthenticated()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]

    def get_queryset(self):
        """Фильтрация объявлений по статусу."""
        if self.request.user.is_superuser:
            return Advertisement.objects.all()
        elif self.request.user.is_authenticated:
            queryset = Advertisement.objects.exclude(status=AdvertisementStatusChoices.DRAFT)
            drafts = Advertisement.objects.filter(creator=self.request.user, status=AdvertisementStatusChoices.DRAFT)
            return queryset | drafts
