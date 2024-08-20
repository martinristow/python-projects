import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

MY_LAT = 41.865021
MY_LONG = 21.943331
weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}


response = requests.get(url=OWM_Endpoint, params=weather_parameters)
print(response.status_code)

response.raise_for_status()

data = response.json()
print(data)
