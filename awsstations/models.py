from django.db import models
from django.contrib.postgres.fields import ArrayField

class AWSStation(models.Model):
    station_id = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    curr_rainfall = models.FloatField(default=0)
    curr_temp = models.FloatField(default=0)
    curr_windspeed = models.FloatField(default=0)
    arr_rainfall = ArrayField(base_field=models.FloatField(), size=30)
    arr_temp = ArrayField(base_field=models.FloatField(), size=30)

    def __str__(self):
        return self.name
    
class StationData(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    rainfall = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    wind_speed = models.FloatField(default=0)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.station.name + " " + str(self.timestamp)


class HourlyPrediction(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pred_rainfall = ArrayField(base_field=models.FloatField(), size=25)

    def __str__(self):
        return self.station.name + " " + str(self.timestamp)

class DailyPrediction(models.Model):
    station = models.ForeignKey(AWSStation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pred_rainfall = ArrayField(base_field=models.FloatField(), size=5)
    day = models.IntegerField(choices=[(1, 'Day 1'), (2, 'Day 2'), (3, 'Day 3')], default=1)

    def __str__(self):
        return self.station.name + " " + str(self.timestamp)

class TrainStation(models.Model):
    
    station_code = models.IntegerField(primary_key=True)
    station_name = models.CharField(max_length=100)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    neareststation = models.ForeignKey( 'AWSStation' , on_delete=models.CASCADE, blank=True, null=True)
    WarningLevel = models.IntegerField(default=0)
    rainfall = ArrayField(base_field=models.FloatField(), size=10)

    def __str__(self):
        return self.station_name
    def update(self):
        last_data = StationData.objects.filter(station=self.neareststation).order_by('-timestamp')[:4]
        if last_data:
            cumulative_rainfall = sum(data.rainfall for data in last_data)
            self.rainfall = [cumulative_rainfall] + list(self.rainfall[:-1])
            
            max_rainfall = max(data.rainfall for data in last_data)
            if max_rainfall > 20:
                self.WarningLevel = 3
            elif max_rainfall > 15:
                self.WarningLevel = 2
            elif max_rainfall > 10:
                self.WarningLevel = 1
            else:
                self.WarningLevel = 0