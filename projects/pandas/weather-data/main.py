with open("weather_data.csv", mode="r") as data_file:
    data = data_file.readlines()
    # print(data)
    for datat in data:
        stripped_data = datat.strip()
        print(stripped_data)
