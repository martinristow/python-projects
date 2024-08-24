from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint



data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()


for city in sheet_data:
    if city["iataCode"] == "":
        flight_search = FlightSearch()
        city["iataCode"] = flight_search.get_iata_code(city["city"])


data_manager.update_sheet_data(sheet_data)
pprint(sheet_data)
