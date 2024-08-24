import requests
from dotenv import load_dotenv
SHEETY_ENDPOINT = "https://api.sheety.co/103066c320884ef5f0776432af28dee6/flightDeals/prices"

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_api = SHEETY_ENDPOINT
        self.sheet_data = None

    def get_sheet_data(self):
        response = requests.get(url=self.sheety_api)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        return self.sheet_data

    def update_sheet_data(self, updated_data):
        for city in updated_data:
            update_endpoint = f"{self.sheety_api}/{city['id']}"
            response = requests.put(url=update_endpoint, json={"price": city})
            response.raise_for_status()


