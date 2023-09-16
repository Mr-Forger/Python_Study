#재귀 함수를 이용해 새 계산 시키기
from art import logo
print(logo)

import os
def clear():
    os.system('cls')

#1. 연산자 함수들 생성
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y
 
def divide(x, y):
    return x/y

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


#재귀 함수를 이용하기
def calculator():
    num1 = int(input("What's the first number?: ")) #파라미터 x에 대응
    flag = True
    #No를 입력하면 다시 실행되게 하세요
    while flag:
        number = int(input("Enter the Another Number.: "))
        choose_op = input("Choose Another Operation: ")
        calculate = operators[choose_op]
        answer = calculate(num1, number)
        print(f"{num1} {choose_op} {number} = {answer}.")
        #여기서 이제 계속 할지 말지 분기를 나눠야 한다.
        ask = input("계속 계산하실꺼면 yes, 그만 계산하실꺼면 no를 입력해주세요.: ")
        if ask == "yes":
            num1 = answer
        elif ask == "no":
            flag = False
            calculator()
            clear()

calculator()






                