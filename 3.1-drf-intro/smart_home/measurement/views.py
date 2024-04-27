from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
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


class InfoSensorView(ListCreateAPIView):
    """
    Информация по датчику
    """
    queryset = Sensors.objects.all()
    serializer_class = InfoSensorSerializer
