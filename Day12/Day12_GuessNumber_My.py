import random
from art import logo

print(logo)


def compare(answer, chance):
    print(f"기회는 총 {chance}번이 주어집니다!")
    while chance != 0:
        guess_number = int(input("숫자를 입력하세요!: "))
        if guess_number > answer:
            print("입력하신 숫자보다 낮습니다!")
            chance -= 1
        elif guess_number < answer:
            print("입력하신 숫자보다 높습니다!")
            chance -= 1
        elif guess_number == answer:
            print("정답입니다!")
            break
        print(f"현재 남은 기회는 {chance} 입니다!")

        if chance == 0:
            print(f"기회가 모두 끝났습니다. 숫자는 {answer} 였습니다!")


flag = True

while flag:
    number = random.randint(1, 100)
    print("숫자 맞추기 게임에 오신 것을 환영합니다!\n")
    print("여러분들이 추측해내셔야 할 숫자의 범위는 1부터 100까지 입니다!")
    if input("난이도를 선택하세요! easy와 hard가 있습니다! ") == "easy":
        attempt = 10
        compare(number, attempt)
    else:
        attempt = 5
        compare(number, attempt)
    if input("게임을 다시 시작하실꺼면 'y' 그만 두실꺼면 'n'을 눌려주세요! ") == "n":
        flag = False

print("고생하셨습니다!")
