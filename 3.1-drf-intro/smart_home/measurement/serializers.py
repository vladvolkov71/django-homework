from rest_framework import serializers
from .models import Sensors, Measurements


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['id', 'sensor_id', 'temperature', 'created_at', 'image']


class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['temperature', 'created_at', 'image']


class InfoSensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(many=True, read_only=True)

    class Meta:
        model = Sensors
        fields = ['id', 'name', 'description', 'measurements']
