# #readlines()를 이용해 리스트화 하는 방법
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data, "\n")
print(data["temp"])