from geopy.geocoders import Nominatim
import requests

def get_weather_info(lat, lon, hourly=True):
    try:
        # We define a condition if we want hourly data
        if hourly:
            url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,weather_code'
        # If we want daily data
        else:
            url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,weather_code&timezone=Europe/Paris'
        
        # We make a GET request to the URL and save it as json()
        response = requests.get(url)
        data = response.json()
        
        if hourly: 
            return data["hourly"] # For hourly data 
        else:
            return data["daily"] # For daily data 
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_coords_from_city(city_name):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        print("Coordinates not found for the given city.")
        return None, None
    

def get_city_coordinates(city_name):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            # Assuming the first result is the most relevant one
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            return float(latitude), float(longitude)
        else:
            print("No results found for the given city name.")
    else:
        print(f"Error: {response.status_code}, {response.text}")


def get_weather_type(weather_code):
    weather_mapping = {
        0: 'Clear sky',
        (1, 2, 3): 'Cloud',
        (45, 48): 'Fog',
        (51, 53, 55): 'Drizzle',
        (56, 57): 'Freezing Drizzle',
        (61, 63, 65): 'Rain',
        (66, 67): 'Freezing Rain',
        (71, 73, 75): 'Snow fall',
        77: 'Snow grains',
        (80, 81, 82): 'Rain showers',
        (85, 86): 'Snow showers',
        95: 'Thunderstorm',
        (96, 99): 'Thunderstorm with slight and heavy hail'
    }

    for key, value in weather_mapping.items():
        if isinstance(key, int):
            if weather_code == key:
                return value
        elif isinstance(key, tuple):
            if weather_code in key:
                return value

    return 'Unknown weather type'


def get_weather_data_from_city(city_name, hour=True):
    coords = get_city_coordinates(city_name)
    return get_weather_info(coords[0], coords[1], hourly=hour)