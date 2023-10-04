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


def check_resrouce(order_ingreidients):
    for item in order_ingreidients:
        if order_ingreidients[item] > resources[item]:
            print(f"죄송합니다. 재료중 현재 {item}이 부족합니다.")
            return False
    return True


def process_coins():
    print("동전을 넣어주세요.")
    totalpay = int(input("쿼터는 몇개 넣으시겠습니까?: ")) * 0.25
    totalpay += int(input("다임즈는 몇개 넣으시겠습니까?: ")) * 0.1
    totalpay += int(input("니클은 몇개 넣으시겠습니까?: ")) * 0.05
    totalpay += int(input("페니는 몇개 넣으시겠습니까?: ")) * 0.01
    return totalpay

def check_transaction(recieve_coins, cost):
    if recieve_coins >= cost:
        change = round(recieve_coins - cost, 2)
        print(f"여기 거스름돈 {change}$ 입니다.")
        global profit
        profit += cost
        return True
    else:
        print("죄송합니다. 돈이 부족합니다. 돈을 반환해드리겠습니다.")
        return False

def make(name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"{name} 나왔습니다! 맛있게 드세요!")


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
    else:
        drink = MENU[choice]
        if check_resrouce(drink["ingredients"]):
            pay = process_coins()
            if check_transaction(pay, drink["cost"]):
                make(choice, drink["ingredients"])


