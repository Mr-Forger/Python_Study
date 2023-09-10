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


