import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""

MY_LAT = 49.567550
MY_LONG = 5.532180
weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(url=OWM_Endpoint, params=weather_parameters)
# print(response.status_code)

response.raise_for_status()

weather_data = response.json()
# print(weather_data)

condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_data["list"]]  # One line code for same situation like bellow

# will_rain = False
# for hour_data in weather_data["list"]: # This is the longer way but code is easier to reading
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring un umbrella.")

# print(condition_code)
for code in condition_code:
    if int(code) < 700:
        print("Bring an Umbrella!")
