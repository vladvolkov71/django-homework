from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensors, Measurements
from .serializers import SensorsSerializer, MeasurementSerializer, InfoSensorSerializer


class UpdateDeleteSensor(RetrieveUpdateDestroyAPIView):
    """
    Изменение и удаление датчиков
    """
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class ListSensor(ListCreateAPIView):
    """
    Список всех датчиков и создание нового датчика
    """
    queryset = Sensors.objects.all()
    serializer_class = SensorsSerializer


class AddMeasurement(CreateAPIView):
    """
    Ввод показаний датчика
    """
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer


class InfoSensorView(APIView):
    """
    Информация по датчику
    """
    # queryset = Sensors.objects.filter(id=id)
    # serializer_class = InfoSensorSerializer
    def get(self, request, id):
        sensor = Sensors.objects.filter(id=id)
        data = InfoSensorSerializer(sensor, many=True).data
        return Response(data)
