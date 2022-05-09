from .models import SensorValue, SensorType, Sensor
from rest_framework import serializers


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ["kind"]


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ["kind", "name", "unit"]


class SensorValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorValue
        fields = ["timestamp", "value", "sensor"]