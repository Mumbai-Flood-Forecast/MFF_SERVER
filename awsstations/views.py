
# Create your views here.
from django.http import JsonResponse

# 1 hr value
#  if any value < 10 green, no flooding
#  if any value >= 10 yellow, possible flooding
#  if any value >= 15 orange, flooding
#  if any value >= 20 red, severe flooding

# views.py
# views.py
from .utils.daily_prediction import predict_day1, predict_day2, predict_day3
from .utils.gfs import download_gfs_data

def get_predictions(request):
    # download_gfs_data()     
    predict_day1()
    # predict_day2()
    # predict_day3()
    return JsonResponse({"status": "success"})