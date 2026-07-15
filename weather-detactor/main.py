from urllib import response

import requests

city_name = input("Enter the city name: ")

def get_weather(city_name):
    base_url = "https://api.openweathermap.org"

    API_KEY = "dfbbb2646e1197843dd024ff24c4b6ae"
    url = f"{base_url}/data/2.5/weather?q={city_name}&appid={API_KEY}"
    
    response = requests.get(url)
    
    data = response.json()
    
    if response.status_code == 200:
        temperature =data['main']['temp']
        humidity =data['main']['humidity']
        weather = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        print("-"*30)
        print("       WEATHER   REPORT       ")
        print("-"*30)
        try:
            city_name = data['name']
            print(f"CITY : {city_name}")        
            print(f"TEMPERATURE : {temperature-273.15:.2f}°C")        
            print(f"FEELS LIKE: {data['main']['feels_like']-273.15:.2f}°C")        
            print(f"HUMIDITY : {humidity}%")        
            print(f"WEATHER : {weather}")        
            print(f"WIND SPEED : {wind_speed} m/s")
        except KeyError:
            print("City not found.")        
        
    else:
            print(f"Error: {data['message']}")
get_weather(city_name)            
  
  
  
