from django.contrib import admin
from .models import AWSStation, DailyPrediction, HourlyPrediction, TrainStation, StationData

admin.site.register(AWSStation)
admin.site.register(DailyPrediction)
admin.site.register(HourlyPrediction)
admin.site.register(TrainStation)
admin.site.register(StationData)
