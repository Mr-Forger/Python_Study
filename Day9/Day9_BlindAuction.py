import os
def clear():
    os.system('cls')

from art import logo
print(logo)

#1. 이름(키) : 입찰가(값)로 이루어진 딕셔너리를 만들어야한다.
bid = {}
auctionFinish = True #옥션이 안끝나면 계속해서 입찰 할 수 있게 한다.

def highestBidder(bidRecord):
    highestBid = 0
    winner = ""

    for bestBidder in bidRecord:
        bidAmount = bidRecord[bestBidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bestBidder
    print(f"The winner is {winner} with a bid of ${highestBid}")


while auctionFinish:
    name = input("What is your name? ")
    bidPrice = int(input("What's your bid?: $"))
    bid[name] = bidPrice
    bidContinue = input("Are there any other bidders? Type 'yes' or 'no'.")

    if bidContinue == "yes":
        clear()
    elif bidContinue == "no":
        auctionFinish = False
        highestBidder(bidRecord=bid)


# 코드 분석:
# Import 구문

    # os 모듈을 가져옵니다. 이 모듈은 OS와 상호작용하기 위한 기능을 제공합니다.
    # from art import logo : art 모듈에서 logo를 가져옵니다. art 모듈은 코드에 포함되지 않았으므로 무엇인지 정확히는 알 수 없습니다. 일반적으로는 아스키 아트나 문자열 아트와 관련된 모듈일 가능성이 있습니다.

# clear 함수

    # 이 함수는 os.system('cls')를 호출하여 콘솔 화면을 지웁니다. 이는 Windows에서 작동하며, Linux나 macOS에서는 'clear'를 사용해야 합니다. OS에 따라 적절한 명령어를 선택하는 것이 좋습니다.

# 변수 및 기본 설정

    # bid : 입찰자의 이름과 그들의 입찰 금액을 저장하는 딕셔너리입니다.
    # auctionFinish : 옥션 진행 여부를 나타내는 변수입니다.
    # print(logo) : 아마도 아스키 아트나 특정 문자열 아트를 화면에 출력하는 것 같습니다.

# highestBidder 함수

    # 파라미터: bidRecord (딕셔너리 타입)
    # 기능: 전달된 딕셔너리에서 가장 높은 입찰액을 가진 입찰자를 찾아 출력합니다.
    # 리턴 값: 없음 (단순히 값을 출력합니다.)
    # 이 함수는 bidRecord라는 딕셔너리를 인자로 받아, 그 중에서 가장 높은 입찰 금액을 가진 입찰자를 찾아 화면에 출력하는 역할을 합니다. 함수 내부에서 for 루프를 사용하여 각 입찰자와 그들의 입찰 금액을 순회하며, 현재까지 찾은 가장 높은 입찰 금액보다 높은 금액을 가진 입찰자가 나타날 때마다 해당 입찰자의 이름과 금액으로 winner와 highestBid를 갱신합니다.

# 주요 루프

    # 사용자로부터 이름과 입찰 금액을 입력 받아 bid 딕셔너리에 저장합니다.
    # 다른 입찰자가 있는지 확인합니다.
    # "yes"라고 응답하면 화면을 지워 다음 입찰자에게 전 입찰자의 정보를 숨깁니다.
    # "no"라고 응답하면 옥션을 종료하고, highestBidder 함수를 호출하여 최고 입찰자를 출력합니다.

# 요약
    # 이 코드는 옥션 시스템을 간단히 구현한 것입니다. 사용자는 이름과 입찰 금액을 입력하며, 옥션에 더 이상 참가할 입찰자가 없을 경우 최고의 입찰액을 가진 입찰자가 출력됩니다.