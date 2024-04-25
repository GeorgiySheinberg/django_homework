from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class Measurement(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=True, auto_created=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
