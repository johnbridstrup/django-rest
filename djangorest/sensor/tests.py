from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import SensorValue, SensorType, Sensor
import uuid


class TestAdminPanel(TestCase):
    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_admin_panel(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            # put all the admin pages for your models in here.
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200
            assert b"<!DOCTYPE html" in resp.content


class SensorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.creator = User.objects.create(id=1, username='test_user')
        cls.sensor_type = "temperature"
        cls.sensorname = "test_sensor"
        cls.unit = "F"
        cls.uuid = uuid.uuid4()
        cls.timestamp = timezone.now()
        cls.value = 98.6

    def test_create_sensortype(self):
        SensorType.objects.create(kind=self.sensor_type)

        sensortype = SensorType.objects.get(id=1)

        self.assertEqual(sensortype.id, 1)
        self.assertEqual(sensortype.kind, self.sensor_type)

    def test_create_sensor(self):
        sensor_type = SensorType.objects.create(kind=self.sensor_type)

        Sensor.objects.create(
            kind=sensor_type, 
            name=self.sensorname,
            unit=self.unit, 
            uuid=self.uuid
        )

        sensor = Sensor.objects.get(id=1)

        self.assertEqual(sensor.id, 1)
        self.assertEqual(sensor.kind.id, sensor_type.id)
        self.assertEqual(sensor.unit, self.unit)
        self.assertEqual(sensor.uuid, str(self.uuid))

    def test_create_sensor_value(self):
        sensor_type = SensorType.objects.create(kind=self.sensor_type)
        sensor = Sensor.objects.create(
            kind=sensor_type, 
            name=self.sensorname,
            unit=self.unit, 
            uuid=self.uuid
        )

        SensorValue.objects.create(
            sensor=sensor,
            timestamp=self.timestamp,
            value=self.value
        )

        sensor_value = SensorValue.objects.get(id=1)

        self.assertEqual(sensor_value.id, 1)
        self.assertEqual(sensor_value.timestamp, self.timestamp)
        self.assertEqual(sensor_value.value, self.value)
        self.assertEqual(sensor_value.sensor.id, sensor.id)

        
