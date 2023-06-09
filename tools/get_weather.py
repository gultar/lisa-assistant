import requests
import geocoder

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.city
    else:
        return "Location not found"

def get_lat_and_long(city):
    # code to get latitude and longitude of city
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather(city="Quebec"):
        
    try:
        data = get_lat_and_long(city)
        if len(data) == 0:
            city = get_current_location()
            data = get_lat_and_long(city)
    except:
        city = get_current_location()
        data = get_lat_and_long(city)
    
    latitude = data[0]['lat']
    longitude = data[0]['lon']

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto"
    response = requests.get(url)
    return response.json()

