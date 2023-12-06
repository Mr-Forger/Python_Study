fruits = eval(input())
# 🚨 위의 코드를 변경하지 마세요

# TODO: 예외를 처리하고 코드가 충돌 없이 실행되도록 하세요.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " 파이")
    except IndexError:
        # print("해당 인덱스에 대한 과일이 없습니다.")
        print("Fruit pie")

# 🚨 아래의 코드를 변경하지 마세요
make_pie(4)
