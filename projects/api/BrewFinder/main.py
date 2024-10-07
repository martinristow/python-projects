import requests

ENDPOINT = 'https://api.openbrewerydb.org/v1/breweries'


def values(response):
    data = response.json()
    for value in data:
        name = value['name']
        type_brewery = value['brewery_type']
        address = value['address_1']
        city_ = value['city']
        state_province = value['state_province']
        country = value['country']
        phone = value['phone']
        street = value['street']
        print(f"Name: {name}")
        print(f"Type: {type_brewery}")
        print(f"Address: {street}, {address}")
        print(f"City: {city_}")
        print(f"State/Province: {state_province}")
        print(f"Country: {country}")
        print(f"Phone: {phone}")
        print("-" * 40)


def all_brewery():
    response = requests.get(url=ENDPOINT)
    values(response)


def find_by_city(city):
    params = {
        'by_city': city
    }

    response = requests.get(url=ENDPOINT, params=params)
    values(response)



def find_by_state(state):
    params = {
        'by_state': state
    }

    response = requests.get(url=ENDPOINT, params=params)
    values(response)



def find_by_brewery_type(brewery_type):
    params = {
        'by_type': brewery_type
    }

    response = requests.get(url=ENDPOINT, params=params)
    values(response)



while True:
    print("\n--- Open Brewery DB Menu ---")
    print("1. View all breweries")
    print("2. Search breweries by city")
    print("3. Search breweries by state")
    print("4. Search breweries by type")
    print("5. Exit")

    select_number = int(input("Enter your choice (1-5):").strip())
    if select_number == 1:
        all_brewery()
    elif select_number == 2:
        city = str(input("Enter a City: "))
        find_by_city(city)
    elif select_number == 3:
        state = str(input("Enter a State: "))
        find_by_state(state)
    elif select_number == 4:
        brewery_type = str(input("Enter a type: "))
        find_by_brewery_type(brewery_type)
    else:
        break
