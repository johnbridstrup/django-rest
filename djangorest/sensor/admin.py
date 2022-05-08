from django.contrib import admin
from .models import SensorType, Sensor, SensorValue


class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ('kind',)
    search_fields = ('kind',)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('get_kind', 'name', 'unit', 'uuid')

    def get_kind(self, obj):
        return obj.kind.kind
    get_kind.admin_order_field = 'kind'
    get_kind.short_description = 'Kind'

class SensorValueAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'value', 'get_unit', 'get_name')

    def get_unit(self, obj):
        return obj.sensor.unit
    get_unit.admin_order_field = 'unit'
    get_unit.short_description = 'Unit'

    def get_name(self, obj):
        return obj.sensor.name
    get_name.admin_order_field = 'name'
    get_name.short_description = 'Name'

admin.site.register(SensorType, SensorTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorValue, SensorValueAdmin)
