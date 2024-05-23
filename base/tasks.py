# weather/tasks.py
from celery import shared_task
from .models import WeatherData
from .utils import MCGM_data
from datetime import datetime, timedelta
import pytz

@shared_task
def fetch_and_store_data():
    data = MCGM_data()
    if data:
        ist = pytz.timezone('Asia/Kolkata')
        utc_now = datetime.utcnow()
        ist_now = utc_now + timedelta(hours=5, minutes=30)  # Adding 5 hours and 30 minutes for IST
        ist_now = ist.localize(ist_now)
        
        WeatherData.objects.create(**data, timestamp=ist_now)
        print(ist_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    else:
        print("Failed to fetch data.")
