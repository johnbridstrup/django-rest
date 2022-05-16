from enum import unique
from django.db import models
import uuid


class SensorType(models.Model):
    kind = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return f"{self.kind}"


class Sensor(models.Model):
    kind = models.ForeignKey(SensorType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)
    unit = models.CharField(max_length=15)
    uuid = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.name} | {self.kind} ({self.unit})"


class SensorValue(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self) -> str:
        return f"{self.sensor.name} | {self.value} ({self.sensor.unit}) @ {self.timestamp}"
