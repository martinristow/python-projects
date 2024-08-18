import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)

# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

# print(response.status_code)
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
# This is really painful way to do this
# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
