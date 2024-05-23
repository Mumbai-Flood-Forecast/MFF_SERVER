# weather/models.py
from django.db import models
from datetime import datetime
import pytz

class WeatherData(models.Model):
    location_id = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    zone_id = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    temp_out = models.FloatField(null=True, blank=True)
    high_temp = models.FloatField(null=True, blank=True)
    low_temp = models.FloatField(null=True, blank=True)
    out_humidity = models.FloatField(null=True, blank=True)
    dew_point = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    wind_dir = models.CharField(max_length=100, null=True, blank=True)
    wind_run = models.FloatField(null=True, blank=True)
    hi_speed = models.FloatField(null=True, blank=True)
    hi_dir = models.CharField(max_length=100, null=True, blank=True)
    wind_chill = models.FloatField(null=True, blank=True)
    heat_index = models.FloatField(null=True, blank=True)
    thw_index = models.FloatField(null=True, blank=True)
    bar = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    rain_rate = models.FloatField(null=True, blank=True)
    head_dd = models.FloatField(null=True, blank=True)
    cool_dd = models.FloatField(null=True, blank=True)
    in_temp = models.FloatField(null=True, blank=True)
    in_humidity = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        ist = pytz.timezone('Asia/Kolkata')
        local_timestamp = self.timestamp.astimezone(ist)
        return local_timestamp.strftime("%Y-%m-%d %H:%M:%S %Z%z")
