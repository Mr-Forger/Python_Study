# # 리스트 컴프리헨션 개요
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers] # 반복문에서 실행 할 코드 + 반복문
# print(new_numbers)

# # 예제1 - 문자열
# name = "moon"
# new_list = [letter for letter in name]
# print(new_list)

# # 예제2 - range
# num = range(1, 5)
# new_list = [n * 2 for n in num]
# print(new_list)

# 조건문 리스트 컴프리헨션
names = ["asadf", "bds", "cdf", "dasdfd", "ed", "f"]
short_name = [n for n in names if len(n) < 4] #이름의 크기가 4 미만인 친구들만 새 리스트에 추가
print(short_name)

#예제3 - 리스트 컴프리헨션 후 대문자로 변환
names = ["asadf", "sbds", "cdddsdf", "dassddfd", "esdsdsdd", "f", "Asdfadsfdsaf", "sdfsfdf"]
long_name = [name.upper() for name in names if len(name) > 5] #반복문 실행 후 수행할 역할을 대문자로 변환되게 지정해준다.
print(long_name)
