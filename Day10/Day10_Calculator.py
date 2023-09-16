from art import logo
print(logo)

#1. 연산자 함수들 생성
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y
 
def divide(X, y):
    return x/y

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("What's the first number?: ")) #파라미터 x에 대응
num2 = int(input("What's the second number?: ")) #파라미터 y에 대응

choose_op = input("choose operation: ")

calculate = operators[choose_op] #연산자 딕셔너리 안의 키 값(연산자)를 고른다.
answer = calculate(num1, num2)

print(f"The {num1} {choose_op} {num2} = {answer}.")




                