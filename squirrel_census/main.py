import pandas
ATTRIBUTE = "Primary Fur Color"

squirrel_info = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": []
}

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for color in squirrel_info["Fur Color"]:
    quantity = len(data[data[ATTRIBUTE] == color][ATTRIBUTE])
    squirrel_info["Count"].append(quantity)

new_data = pandas.DataFrame(squirrel_info)
new_data.to_csv("./squirrel_count.csv")

