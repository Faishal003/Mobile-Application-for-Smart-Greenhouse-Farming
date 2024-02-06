from django.db import models
from django.contrib.auth.models import User

class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()

    def __str__(self):
        return str(self.id)

class SensorTable(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    soil_moisture = models.FloatField()

    def __str__(self):
        return str(self.farm.id) + " " + str(self.temperature) + " " + str(self.humidity) + " " + str(self.ph)
