# # with open("weather_data.csv", mode="r") as data_file:
# #     data = data_file.readlines()
# #     # print(data)
# #     for datat in data:
# #         stripped_data = datat.strip()
# #         print(stripped_data)
#
# # THIS WAY IS SO PAINFUL IF WE HAVE A LOT OF DATA
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     temperature = []
# #     data = csv.reader(data_file)
# #     # print(data)
# #     # next(data) # first row is jumped
# #     for row in data:
# #         if row[1] != "temp":
# #             # print(row[1])
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
#
# # PANDAS FRAMEWORK
import pandas

data = pandas.read_csv("weather_data.csv")
# # print(type(data)) # The entire table is called a DataFrame
# # temperatures = data["temp"]
# # print(type(temperatures)) # One row is called a Series
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average_temp = data["temp"].mean()  # The mean() function returns an average number
# # print(average_temp)
# max_temp = data["temp"].max()  # The max() function returns the highest temperature in our list
# print(max_temp)
#
# # Get Data in Columns
# print(data["condition"])  # These two ways work the same
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)
monday_temp = monday.temp[0]
# print(monday_temp)
# F= (C*9 /5) + 32
monday_temp_F = (monday_temp * 9 / 5) + 32
print(monday_temp_F)


