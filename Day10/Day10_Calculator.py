from art import logo
print(logo)

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

#입력 값 생성
num1 = int(input("What's the first number?: ")) #파라미터 x에 대응
num2 = int(input("What's the second number?: ")) #파라미터 y에 대응

choose_op = input("choose operation: ")
calculate = operators[choose_op]
print(f"{num1} {choose_op} {num2} = {calculate}.")

#calculate 값을 받아서 다시 연산하는 코드를 작성하세요.

                