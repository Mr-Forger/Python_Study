# #readlines()를 이용해 리스트화 하는 방법
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import pandas

data = pandas.read_csv("weather_data.csv")
# #판다스로 csv 파일 출력하기
# print(data, "\n")
# print(data["temp"])

# #데이터 타입 확인하기
# #DataFrame = 전체 표와 같다.(스프레드 시트도 데이터 프레임으로 간주)
# print(type(data))
# print(type(data["temp"])) #Series = 열을 나타내며 파이썬 리스트와 같다고 보면 된다.

# # 리스트 또는 딕셔너리화 시키기
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list() #특정 시리즈를 리스트로 변환하기

# # #challenge 1: 온도 열의 평균 구하기
# temp_avg = sum(temp_list) / len(temp_list)
# print(round(temp_avg))
# print(data["temp"].mean())  # mean()메소드로 평균을 바로 구할 수 있다. 참고로 mean은 평균이란 뜻이다. 의미는 meaning이다.

# # challenge 2: 온도 열의 최고 값 구하기
# print(data["temp"])
# print(data["temp"].max())  # max()메소드로 최곳값을 바로 구할 수 있다.

# # 열에서 데이터 추출하기
# print(data["condition"]) # 이 방법은 딕셔너리에 가깝게 사용한다.
# print(data.condition) # 이 방법은 객체에 가깝게 사용한다.

# # 행에서 데이터 추출하기(열보다 좀 더 어렵다.)
# print(data[data.day == "Monday"])

# #challenge 3: 가장 높은 온도가 있는 행을 추출하기
# print(data[data.temp == data.temp.max()])

# # 특정 행을 변수로 지정하고 해당 행에서 데이터 추출하기
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # challenge 4: 월요일의 온도를 불러와서 화씨로 바꾸기
# monday_row = data[data.day == "Monday"]
# print(monday_row)
# monday_temp = monday_row.temp
# print(monday_temp)
# monday_temp_F = (9/5)*monday_temp + 32
# print(int(monday_temp_F))

# # 파일 불러오기가 아닌 파이썬 내부에서 데이터프레임 만들고 해당 데이터프레임을 csv파일화 시키기
# data_dict = {
#     "names": ["a", "b", "c"],
#     "scores": [90, 80, 70],
# }
#
# dict_to_dataframe = pandas.DataFrame(data_dict)
# print(dict_to_dataframe)
# dict_to_dataframe.to_csv("new_data.csv")
