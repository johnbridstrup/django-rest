from .models import SensorValue, Sensor, SensorType
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializers import SensorSerializer, SensorTypeSerializer, SensorValueSerializer
from .utils import sendresponse, verify_keys
from .models import Sensor, SensorValue


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


class SensorValueViewSet(CreateAPIView):
    """
    API endpoint that allows sensor values to be created.
    """
    queryset = SensorValue.objects.all().order_by('timestamp')
    serializer_class = SensorValueSerializer
    permission_classes = [permissions.IsAuthenticated]
    post_keys = ["value", "timestamp", "uuid"]
    def post(self, request):
        try:
            message = {}
            verify_keys(self.post_keys, request, message)

            uuid = request.data.pop("uuid")
            sensor = Sensor.objects.get(pk=uuid)
            value = SensorValue.objects.create(**request.data, sensor=sensor)
            return sendresponse(
                response_status="success",
                response_message="Value created successfully",
                response_data=SensorValueSerializer(value, context={'request': request}).data,
                status_code=200)
        except Exception as e:
            return sendresponse(
                response_status='error',
                response_message={**message, "exception": str(e)},
                response_data={},
                status_code=400)

    def get(self, request):
        sensorvalues = SensorValue.objects.all()
        serializer = SensorValueSerializer(sensorvalues, many=True, context={'request': request})
        return sendresponse(
            response_status="success",
            response_message="Values retrieved successfully",
            response_data=serializer.data,
            status_code=200)
