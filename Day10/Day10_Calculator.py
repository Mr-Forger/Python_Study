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
print(f"{num1} {choose_op} {num2} = {first_answer}.")

#calculate 값을 받아서 다시 연산하는 코드를 작성하세요.
choose_op = input("Choose another operation: ")
num3 = int(input("What's the another number?: "))
calculate = operators[choose_op]
second_answer = calculate(calculate(num1, num2), num3) #calculate는 딕셔너리에 저장된 함수를 실행하는 것이기 때문에 함수로 적어도 된다.
print(f"{first_answer} {choose_op} {num3} = {second_answer}.")

calculate = operators[choose_op] #연산자 딕셔너리 안의 키 값(연산자)를 고른다.
answer = calculate(num1, num2)

print(f"The {num1} {choose_op} {num2} = {answer}.")




                