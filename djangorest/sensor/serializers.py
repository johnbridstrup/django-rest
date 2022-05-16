from .models import SensorValue, SensorType, Sensor
from rest_framework import serializers


class SensorTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorType
        fields = ["kind"]

    def create(self, validated_data):
        kind_input = validated_data.pop('kind')

        kind = kind_input.lower()
        sensor_type_obj = SensorType.objects.create(kind=kind)
        return sensor_type_obj


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    kind = serializers.CharField()
    class Meta:
        model = Sensor
        fields = ["kind","name", "unit", "uuid"]

    def create(self, validated_data):
        sensor_type_data = validated_data.pop('kind')
        sensor_type, created = SensorType.objects.get_or_create(kind=sensor_type_data)
        # validated_data['kind'] = sensor_type
        sensor_obj = Sensor.objects.create(**validated_data, kind=sensor_type)
        return sensor_obj

class SensorValueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorValue
        fields = ["timestamp", "value", "sensor"]

    def create(self, validated_data):
        sensor = validated_data.pop('sensor')
        print(sensor)
        if isinstance(sensor, Sensor):
            print("creating with object")
            sensor_val_obj = SensorValue.objects.create(**validated_data, sensor=sensor)
        else:
            print("creating with uuid")
            sensor_obj = Sensor.objects.get(pk=sensor)
            sensor_val_obj = SensorValue.objects.create(**validated_data, sensor=sensor_obj)
        
        return sensor_val_obj