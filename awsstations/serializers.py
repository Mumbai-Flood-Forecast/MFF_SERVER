from rest_framework import serializers
from .models import AWSStation, StationData, HourlyPrediction, DailyPrediction, TrainStation

class AWSStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AWSStation
        fields = '__all__'

class StationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationData
        fields = ['rainfall', 'timestamp']