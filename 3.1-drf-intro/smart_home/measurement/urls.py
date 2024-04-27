from django.urls import path

from .views import ListSensor, UpdateDeleteSensor, InfoSensorView, AddMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', ListSensor.as_view()),
    path('sensors/<int:pk>/', InfoSensorView.as_view()),
    path('sensors/<int:pk>/<str:sensor_description>/', UpdateDeleteSensor.as_view()),
    path('sensors/<str:sensor_name>/<str:sensor_description>/', ListSensor.as_view()),
    path('measurements/<int:pk>/<str:temperature>/', AddMeasurement.as_view()),
]