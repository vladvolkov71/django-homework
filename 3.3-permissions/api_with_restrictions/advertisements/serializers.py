from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        if self.context["request"].method == "POST":
            if Advertisement.objects.filter(creator=self.context["request"].user,
                                            status=AdvertisementStatusChoices.OPEN).count() >= 10:
                raise serializers.ValidationError("Вы не можете создать больше 10 открытых объявлений")

        return data
