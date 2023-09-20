from art import logo

print(logo)

import random

number = random.randint(1, 100)
attempt = 5
flag = True


def easy():
    global attempt
    attempt = 10
    while attempt != 0:
        guess_number = int(input("숫자를 입력하세요!: "))
        if guess_number > number:
            print("입력하신 숫자보다 낮습니다!")
            attempt -= 1
        elif guess_number < number:
            print("입력하신 숫자보다 높습니다!")
            attempt -= 1
        elif guess_number == number:
            print("정답입니다!")
            break
        print(f"현재 남은 기회는 {attempt} 입니다!")

        if attempt == 0:
            print(f"기회가 모두 끝났습니다. 숫자는 {number} 였습니다!")


def hard():
    global attempt
    attempt = 5
    while attempt != 0:
        guess_number = int(input("숫자를 입력하세요!: "))
        if guess_number > number:
            print("입력하신 숫자보다 낮습니다!")
            attempt -= 1
        elif guess_number < number:
            print("입력하신 숫자보다 높습니다!")
            attempt -= 1
        elif guess_number == number:
            print("정답입니다!")
            break
        print(f"현재 남은 기회는 {attempt} 입니다!")

        if attempt == 0:
            print(f"기회가 모두 끝났습니다. 숫자는 {number} 였습니다!")


while flag:
    print("숫자 맞추기 게임에 오신 것을 환영합니다!\n")
    print("여러분들이 추측해내셔야 할 숫자의 범위는 1부터 100까지 입니다!")
    if input("난이도를 선택하세요! easy와 hard가 있습니다! ") == "easy":
        easy()
    else:
        hard()
    if input("게임을 다시 시작하실꺼면 'y' 그만 두실꺼면 'n'을 눌려주세요") == "n":
        flag = False

print("고생하셨습니다!")


