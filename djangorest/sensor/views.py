from .models import SensorValue, Sensor, SensorType
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SensorSerializer, SensorTypeSerializer, SensorValueSerializer


class SensorTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensor types to be viewed or edited.
    """
    queryset = SensorType.objects.all().order_by('kind')
    serializer_class = SensorTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sensors to be viewed or edited.
    """
    queryset = Sensor.objects.all().order_by('name')
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]


class SensorValueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SensorValue.objects.all().order_by('timestamp')
    serializer_class = SensorValueSerializer
    permission_classes = [permissions.IsAuthenticated]
