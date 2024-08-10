# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     # print(data)
#     for datat in data:
#         stripped_data = datat.strip()
#         print(stripped_data)

# THIS WAY IS SO PAINFUL IF WE HAVE A LOT OF DATA
import csv

with open("weather_data.csv") as data_file:
    temperature = []
    data = csv.reader(data_file)
    # print(data)
    # next(data) # first row is jumped
    for row in data:
        if row[1] != "temp":
            # print(row[1])
            temperature.append(int(row[1]))
    print(temperature)
