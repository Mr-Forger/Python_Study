# #파일을 찾을 수 없는 경우
# with open("ex1.txt") as file:
#     file.read()

# # 키 오류
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

# # 인덱스 오류
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# # 타입 오류
# text = "Abc"
# print(text + 5)

# 파일을 찾지 못했을 때
try:
    file = open("a_file.txt")
except:
    print("There was an error")