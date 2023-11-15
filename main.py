import json
from src.weather_data_process import get_weather_data_from_city

def save_to_json(data):
    with open("weather_data.json", "w") as f:
        json.dump(data, f)

def main():
    cities = ["Barcelona", "New-York", "New-Dehli", "Paris"]

    weather_data = []
    for city in cities:
        city_info = {"city": city}
        city_info["data"] = get_weather_data_from_city(city, hour=False)
        weather_data.append(city_info)
    print(weather_data)
    save_to_json(weather_data)
            
if __name__ == "__main__":
    main()

