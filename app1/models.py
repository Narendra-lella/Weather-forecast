
from django.db import models

# Create your models here.


class WeatherData(models.Model):
    description = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    feels_like = models.FloatField()
    location = models.CharField(max_length=100)
    datetime=models.DateTimeField(auto_now_add=True)



