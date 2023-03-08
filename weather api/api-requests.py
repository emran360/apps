import requests
import json


def weather_api(city):
    api_key = 'e62d41e55f9be4eeeeb1a89ce9f253de'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    results = {}
    results['lon'] = data['coord']['lon']
    results['lat'] = data['coord']['lat']
    results['name'] = data['name']
    results['timezone'] = data['timezone']
    results['temp'] = data['main']['temp']
    results['temp_min'] = data['main']['temp_min']
    results['temp_max'] = data['main']['temp_max']
    results['humidity'] = data['main']['humidity']
    return results
print(weather_api('london'))
