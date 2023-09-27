MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resrouce(ingridients):
    for


flag = True
while flag:
    choice = input("에스프레소, 라떼, 카푸치노 중 어떤 것을 드시겠습니까?: ")
    #choice가 off 일때 프로그램 종료
    if choice == "off":
        flag = False
    elif choice == "report":
        print(f"현재 물의 양은: {resources['water']}ml 입니다.") #F-String에서는 딕셔너리를 작은 따옴표로 묶어야지 이상이 없다.
        print(f"현재 우유의 양은: {resources['milk']}ml 입니다.")
        print(f"현재 커피의 양은: {resources['coffee']}g 입니다.")
        print(f"현재 자판기에 돈은 {profit}$가 있습니다.")
