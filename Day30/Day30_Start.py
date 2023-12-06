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

# # 파일을 찾지 못했을 때
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file.txt", "w")
#     file.write("Something")

# # 예외에 조건 추가와 오류 메세지 출력, 그리고 else와 finally
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError: # a_file이 존재하기 때문에 해당 예외는 실행되지 않는다.
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message: # keyerror가 발생했기에 해당 예외가 실행된다. / error_message: 예외가 발생했을 때 해당 예외에서 생성된 오류 메세지를 출력
#     print(f"The key {error_message} does not exist.")
# else: # try에서 예외가 발생하지 않으면 else로 넘어간다
#     content = file.read()
#     print(content)
# finally: # else와 다르게 모든 어떠한 경우가 발생해도 실행된다
#     # file.close()
#     # print("File was closed.")
#     raise KeyError("내가 만든 에러입니다.") # raise를 이용해 나만의 에러 만들기

height = float(input("키: "))
weight = int(input("몸무게: "))

if height > 3:
    raise ValueError("사람의 키는 3미터를 넘어갈 수 없습니다!")

bmi = weight / height ** 2
print(bmi)
