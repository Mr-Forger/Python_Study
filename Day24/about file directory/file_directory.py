# with open("my_file.txt") as file: # with 열린 파일 as 파일명(일종의 변수) / close메소드가 필요없다.
#     contents = file.read() #read 메소드는 파일 내 컨텐츠를 문자열로 반환한다.
#     print(contents)
# # file.close() #꼭 닫아야지 컴퓨터의 자원을 쓸데없이 안잡아먹는다.


# #기존 txt파일 안의 내용을 지우고 새 내용을 넣고 싶을 때
# with open("my_file.txt", mode="w") as file: #open메소드는 기본적으로 읽기전용(mode="r")이기 때문에 쓰기전용으로 바꿔줘야한다.
#     file.write("New Text!")

# #기존 txt파일 안의 내용을 냅두고 새 내용을 추가하고 싶을 때
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text!")

# txt파일을 폴더 내 경로가 아닌 더 상위 경로로 옮겼을때 실행시키기
with open("../../../../../../Users/USER/OneDrive/바탕 화면/my_file.txt") as file:
    content = file.read()
    print(content)
