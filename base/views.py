# weather/views.py
from django.http import HttpResponse
from openpyxl import Workbook
from .models import WeatherData

def weather_data_excel(request):
    # Fetch all WeatherData objects
    data_objects = WeatherData.objects.all()

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Add headers
    headers = [
        "Location ID", "Code", "Description", "Zone ID", "Latitude",
        "Longitude", "Status", "Temp Out", "High Temp", "Low Temp",
        "Out Humidity", "Dew Point", "Wind Speed", "Wind Dir", "Wind Run",
        "Hi Speed", "Hi Dir", "Wind Chill", "Heat Index", "THW Index",
        "Bar", "Rain", "Rain Rate", "Head DD", "Cool DD", "In Temp",
        "In Humidity", "Timestamp"
    ]
    ws.append(headers)

    # Add data rows
    for obj in data_objects:
        row = [
            obj.location_id, obj.code, obj.description, obj.zone_id, obj.latitude,
            obj.longitude, obj.status, obj.temp_out, obj.high_temp, obj.low_temp,
            obj.out_humidity, obj.dew_point, obj.wind_speed, obj.wind_dir, obj.wind_run,
            obj.hi_speed, obj.hi_dir, obj.wind_chill, obj.heat_index, obj.thw_index,
            obj.bar, obj.rain, obj.rain_rate, obj.head_dd, obj.cool_dd, obj.in_temp,
            obj.in_humidity, obj.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        ]
        ws.append(row)

    # Save the workbook to a response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=weather_data.xlsx'
    wb.save(response)

    return response
