import requests

def get_weather(city):
    # code to get latitude and longitude of city
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    latitude = data[0]['lat']
    longitude = data[0]['lon']

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto"
    response = requests.get(url)
    return response.json()

