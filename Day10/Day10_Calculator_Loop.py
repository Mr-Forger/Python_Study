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
first_answer = calculate(num1, num2)
answer = first_answer
print(f"{num1} {choose_op} {num2} = {first_answer}.")

#No를 입력하기 전까지 계속해서 연산이 될 수 있게 하세요
flag = True
while flag:
    number = int(input("Enter the Another Number.: "))
    choose_op = input("Choose Another Operation: ")
    calculate = operators[choose_op]
    another_answer = calculate(answer, number)
    print(f"{}")



                