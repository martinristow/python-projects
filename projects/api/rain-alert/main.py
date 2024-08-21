import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""
account_sid = ""
auth_token = ""

MY_LAT = 50.264893
MY_LONG = 19.023781

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

will_rain = False
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
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring un Umbrella.",
        from_="",
        to=""
    )
    print(message.status)
