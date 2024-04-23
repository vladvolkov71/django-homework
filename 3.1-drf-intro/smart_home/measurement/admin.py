from django.contrib import admin

from measurement.models import Sensors, Measurements


# Register your models here.

@admin.register(Sensors)
class SensorsAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    pass
