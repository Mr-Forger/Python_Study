import random
from art import logo
print(logo)

import os
def clear():
    os.system('cls')
#셔플
def shuffle():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] #카드 덱 생성
    shuffle_card = random.choice(cards) #셔플한 카드에서 랜덤으로 하나 뽑는다.
    return shuffle_card #하나 뽑고 함수 종료


#점수 계산
def score(final_cards):
    if sum(final_cards) == 21 and len(final_cards) == 2: #블랙잭인 경우
        return 0
    
    if 11 in final_cards and sum(final_cards) > 21: #에이스를 뽑았는데 합계가 21이 초과할때 에이스의 값을 1로 바꾼다.
        final_cards.remove(11)
        final_cards.append(1)
    return sum(final_cards)

        

#결과 여부
def versus(player_score, dealer_score):
    #1. 내 카드의 합이 21을 넘을때
    if player_score and dealer_score > 21:
        return "You Lose."
    if player_score == dealer_score:
        return "Draw."
    elif player_score > 21:
        return "You Lose."
    elif dealer_score > 21 and player_score < 21:
        return "You Win."
    elif player_score > dealer_score:
        return "You Win."
    else: #player_score < dealer_score 인 경우
        return "You Lose"

#블랙잭 플레이
def play():
    player_cards = []
    dealer_cards = []
    flag = True

    for i in range(2): #최초 실행시 카드 두장을 플레이어와 딜러에게 준다.
        player_cards.append(shuffle())
        dealer_cards.append(shuffle())

    while flag: # flag가 True일때 블랙잭 게임을 돌리자.
        player_score = score(player_cards) #두장 카드의 합을 score 함수로 보내기
        dealer_score = score(dealer_cards)
        print(f"Your Cards {player_cards}, Now your score is {player_score} ") #플레이어의 첫 두장의 카드는 모두 공개한다.
        print(f"dealer's first card is {dealer_cards[0]}") #딜러의 카드는 한장만 먼저 공개한다.

        #여기서 카드를 더 받을지(히트), 그만 받을지 분기를 나눈다. 주의해야 할 점은 블랙잭이거나, 내 점수가 21이 넘어가면 그냥 게임이 종료되어야 한다.
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            flag = False #반복문 종료
        else:
            ask_hit = input("Are you want hit? or finish. if you want hit press 'h' or finish press 'n'")
            if ask_hit == "h":
                player_cards.append(shuffle())
            else:
                flag = False #반복문 종료

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(shuffle())
        dealer_score = score(dealer_cards)
    
    print(f"Final Player's Cards and Scores are {player_cards}, {player_score}")
    print(f"Final Dealer's Cards and Socres are {dealer_cards}, {dealer_score}")
    print(versus(player_score, dealer_score))

while input("If you play Blackjack again press 'y' or finish press 'n'") == "y":
    clear()
    play()

print("Finish!")


    





