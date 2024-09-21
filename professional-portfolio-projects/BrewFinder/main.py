import requests

ENDPOINT = 'https://api.openbrewerydb.org/v1/breweries'



def all_brewery():
    response = requests.get(url=ENDPOINT)
    data = response.json()
    for value in data:
        name = value['name']
        type_brewery = value['brewery_type']
        address = value['address_1']
        city_ = value['city']
        state_province = value['state_province']
        country = value['country']
        phone = value['phone']
        state = value['state']
        street = value['street']
        print(f"{name}\n"
              f"{street}\n"
              f"{city_}\n"
              f"{country}\n"
              f"{phone}\n")


def find_by_city(city):
    params = {
        'by_city': city
    }

    response = requests.get(url=ENDPOINT, params=params)
    data = response.json()
    for value in data:
        print(value['city'])



def find_by_state(state):
    params = {
        'by_state': state
    }

    response = requests.get(url=ENDPOINT, params=params)
    data = response.json()
    for value in data:
        print(value['state'])



def find_by_brewery_type(brewery_type):
    params = {
        'by_type': brewery_type
    }

    response = requests.get(url=ENDPOINT, params=params)
    data = response.json()
    for value in data:
        print(value['brewery_type'])



while True:
    print("If you want to see all breweries, choose 1.")
    print("If you want to search for a brewery by city, choose 2.")
    print("If you want to search for a brewery by state, choose 3.")
    print("If you want to search for a brewery by type, choose 4.")
    print("Press 5 to exit.")

    select_number = int(input())
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
