# Nesting
capitals = {
    "France" : "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a Dictionary
travel = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Macedonia" : ["Skopje", "Sveti Nikole", "Shtip"]
}


# Nested Dictionary in a Dictionary
travel_log = {
    "France" : {"cities_visited" : ["Paris","Lille","Dijon"], "total_visits":12},
    "Francee" : {"cities_visited" : ["Skopje","Sveti Nikole","Shtip"] , "total_visits": 75}
}
# print(travel_log)

# Nested Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited" : ["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
        "country": "Macedonia",
        "cities_visited" : ["Skopje","Sveti Nikole","Shtip"],
        "total_visits": 75
     }
]

print(travel_log)

for i in travel_log:
    print(i["cities_visited"])