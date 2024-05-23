import requests

stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 56, 59, 60, 61, 62, 63, 64, 65, 66, 67]




def MCGM_data():
    url = "https://dmwebtwo.mcgm.gov.in/api/tabWeatherForecastData/loadById"
    headers = {
        "Authorization": "Basic RE1BUElVU0VSOkRNYXBpdXNlclBhJCR3b3JkQDEyMzQ="
    }
    
    for station in stations :
        payload = {"id": station}
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            location_data = data['locationList']
            dummy_data = data['dummyTestRaingaugeDataDetails']
            
            result = {
                'location_id': location_data['id'],
                'code': location_data['code'],
                'description': location_data['description'],
                'zone_id': location_data['zoneid'],
                'latitude': location_data['lati'],
                'longitude': location_data['longi'],
                'status': location_data['status'],
                'temp_out': None if dummy_data['tempOut'] == '---' else dummy_data['tempOut'],
                'high_temp': None if dummy_data['highTemp'] == '---' else dummy_data['highTemp'],
                'low_temp': None if dummy_data['lowTemp'] == '---' else dummy_data['lowTemp'],
                'out_humidity': None if dummy_data['outHumidity'] == '---' else dummy_data['outHumidity'],
                'dew_point': None if dummy_data['dewPoint'] == '---' else dummy_data['dewPoint'],
                'wind_speed': None if dummy_data['windSpeed'] == '---' else dummy_data['windSpeed'],
                'wind_dir': None if dummy_data['windDir'] == '---' else dummy_data['windDir'],
                'wind_run': None if dummy_data['windRun'] == '---' else dummy_data['windRun'],
                'hi_speed': None if dummy_data['hiSpeed'] == '---' else dummy_data['hiSpeed'],
                'hi_dir': None if dummy_data['hiDir'] == '---' else dummy_data['hiDir'],
                'wind_chill': None if dummy_data['windChill'] == '---' else dummy_data['windChill'],
                'heat_index': None if dummy_data['heatIndex'] == '---' else dummy_data['heatIndex'],
                'thw_index': None if dummy_data['thwIndex'] == '---' else dummy_data['thwIndex'],
                'bar': None if dummy_data['bar'] == '---' else dummy_data['bar'],
                'rain': None if dummy_data['rain'] == '---' else dummy_data['rain'],
                'rain_rate': None if dummy_data['rainRate'] == '---' else dummy_data['rainRate'],
                'head_dd': None if dummy_data['headDd'] == '---' else dummy_data['headDd'],
                'cool_dd': None if dummy_data['coolDd'] == '---' else dummy_data['coolDd'],
                'in_temp': None if dummy_data['inTemp'] == '---' else dummy_data['inTemp'],
                'in_humidity': None if dummy_data['inHumidity'] == '---' else dummy_data['inHumidity']
            }
            return result
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
