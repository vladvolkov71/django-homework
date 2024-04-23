# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response as Response
from rest_framework.views import APIView

from .models import Sensors, Measurements
from .serializers import SensorsSerializer, MeasurementSerializer


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensors.objects.all()
        data = SensorsSerializer(sensors, many=True).data
        return Response(data)

    def post(self, request, sensor_name, sensor_description):
        sensor = Sensors.objects.create(name=sensor_name, description=sensor_description)
        sensor.save()
        data = SensorsSerializer(sensor).data
        return Response(data)

    def patch(self, request, sensor_id, sensor_description):
        sensor = Sensors.objects.get(id=sensor_id)
        sensor.description = sensor_description
        sensor.save()
        data = SensorsSerializer(sensor).data
        return Response(data)


class MeasurementView(APIView):
    def post(self, request, sensor_id, temp_value):
        sensor = Sensors.objects.get(id=sensor_id)
        measurement = Measurements.objects.create(sensor_id=sensor, temperature=float(temp_value))
        measurement.save()
        data = MeasurementSerializer(measurement).data
        return Response(data)

    def get(self, request, sensor_id):
        measurements = Measurements.objects.filter(sensor_id=sensor_id)
        data = MeasurementSerializer(measurements, many=True).data
        return Response(data)
