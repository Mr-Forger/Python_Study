from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

flag = True

while flag:
    options = menu.get_items()
    choice = input(f"어떤 메뉴를 선택하시겠습니까? {options}: ")
    if choice == "off":
        flag = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



# CoffeeMaker 클래스:
#
# __init__: 초기화 함수에서는 커피 머신의 자원 (물, 우유, 커피)의 초기 수치를 설정합니다. 처음에는 물 300ml, 우유 200ml, 커피 100g이 있습니다.
# report: 이 메서드는 현재 머신 내의 자원 상태를 출력합니다.
# is_resource_sufficient: 사용자가 선택한 음료를 만들기 위한 자원이 충분한지 확인합니다. 만약 부족한 자원이 있다면, 해당 자원이 부족하다는 메시지를 출력하고 False를 반환합니다.
# make_coffee: 음료를 제조하기 위해 필요한 재료의 양을 머신의 자원에서 차감하고, 음료 제조 완료 메시지를 출력합니다.
# MenuItem 클래스:
#
# 이 클래스는 메뉴의 각 아이템을 나타냅니다. 각 아이템에는 이름, 필요한 재료와 가격 정보가 있습니다.
# Menu 클래스:
#
# __init__: 초기화 함수에서는 라떼, 에스프레소, 카푸치노와 같은 다양한 메뉴 아이템을 생성하고 이를 메뉴 목록에 추가합니다.
# get_items: 사용 가능한 모든 음료의 이름을 반환합니다. 이것은 사용자에게 음료 옵션을 보여주는 데 사용됩니다.
# find_drink: 주어진 음료 이름을 가진 MenuItem 객체를 반환합니다. 만약 해당 이름의 음료가 없다면, 사용 가능하지 않다는 메시지를 출력합니다.
# MoneyMachine 클래스:
#
# __init__: 초기화 함수에서는 이익과 받은 돈을 0으로 설정합니다.
# report: 현재 이익을 화폐 단위로 출력합니다.
# process_coins: 사용자로부터 동전을 받아들이고, 총 금액을 계산합니다.
# make_payment: 주어진 비용을 지불하기 위해 충분한 돈이 들어왔는지 확인하고, 너무 많은 돈이 들어온 경우 거스름돈을 반환합니다.
# 마지막 부분의 코드는 실제 프로그램의 실행 흐름을 나타냅니다:
#
# Menu, CoffeeMaker, MoneyMachine 객체를 생성합니다.
# 무한 루프 내에서 사용자에게 음료를 선택하도록 요청합니다.
# "off"를 선택하면 프로그램을 종료하고, "report"를 선택하면 현재 자원 및 이익 상태를 출력합니다.
# 다른 음료를 선택하면, 머신에서 해당 음료를 제조할 수 있는지 자원을 확인하고, 충분한 돈을 받았는지 확인한 후 음료를 제조하고 제공합니다.
# 이렇게 복잡한 프로세스를 클래스와 메서드로 나누어 구현함으로써, 각 기능을 독립적으로 관리하고 코드의 가독성과 유지 보수성을 높였습니다.