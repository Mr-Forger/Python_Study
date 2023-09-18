from art import logo
print(logo)

import os
def clear():
    os.system('cls')

#딕셔너리를 활용 해 익명 경매 프로그램을 만드세요.
bidder = {} #이름(키) : 입찰가(값)으로 이루어진 딕셔너리 만들기.
flag = True

def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""

    for best_bidder in bid_record:
        bid_amount = bid_record[best_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = best_bidder
    print(f"승자는 {winner}입니다! 낙찰가는{highest_bid}$ 입니다!")

#추가 입찰자가 있을시 계속해서 입찰을 받을 수 있게 하기
while flag:
    name = input("이름: ")
    bidprice = int(input("입찰가를 입력하세요: $"))
    bidder[name] = bidprice  # bidder 딕셔너리의 name(키)의 값은 bidprice이다.

    bid_continue = input("다른 입찰자가 있으면 yes, 없으면 no를 입력해주세요: ")

    if bid_continue == "yes":
        clear() #화면 없애고 다음 사람 입찰받기.
    else:
        flag = False
        highest_bidder(bidder)
