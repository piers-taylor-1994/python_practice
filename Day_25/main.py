import pandas

# data = ""
# with open("Day_25/weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv
# with open("Day_25/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("Day_25/weather_data.csv")
# #print(data["temp"])

# #Dataframe methods (table)
# data_dict = data.to_dict()
# print(data_dict)

# #Series methods (columns)
# temp_list = data["temp"].to_list()
# print(temp_list)

# #Use in-built panda methods
# print(data["temp"].mean())
# print(data["temp"].max())

# #Find a row
# print(data[data["day"] == "Monday"])

# # print(data[data["temp"] == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# #Find the value of a column
# print((data[data.day == "Monday"].temp[0] * 9 / 5) + 32)

#Create a dataframe
# data_dict = {
#     "Students": ["Piers", "Jill", "Jacob"],
#     "Scores": [90, 99, 85]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Day_25/students.csv")

with open("Day_25/squirrels.csv") as file:
    data = pandas.read_csv(file)

grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Day_25/squirrel_count.csv")