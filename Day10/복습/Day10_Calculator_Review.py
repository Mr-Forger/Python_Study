from art import logo
print(logo)

import os
def clear():
    os.system('cls')
#첫번째 수, 두번째 수, 연산자 선택 후 연산 진행
#y 또는 n을 클릭 해 계산을 계속 할지 계산을 초기화 할지 선택한다.

#연산 함수 생성
def add(x, y):
    return x+y
def subtract(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y

#딕셔너리를 이용해서 연산자 선택 시 딕셔너리 내의 value값이 실행 될 수 있게 한다.
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("첫번째 숫자를 입력하세요: "))
    flag = True
    #두번째 수는 계산을 계속해서 진행할 때 두번째 수를 계속해서 입력 할 수로 이용하게 해야한다.
    while flag:
        num2 = int(input("계산을 할 다른 숫자를 입력하세요: "))
        select_op = input("사용할 연산자를 입력하세요: ")
        calculate = operation[select_op]
        answer = calculate(num1, num2) #정답은 딕셔너리 내의 선택한 연산자의 value이다. value는 함수이므로 함수의 파라미터를 넣어도 된다.
        print(f"{num1} {select_op} {num2} = {answer}")

        if input("계산을 계속하실꺼면 'y', 그만하실꺼면 'n'을 입력해주세요: ") == "y":
            num1 = answer
        else:
            flag = False
            clear()
            calculator()

calculator() #최초 연산 실행




