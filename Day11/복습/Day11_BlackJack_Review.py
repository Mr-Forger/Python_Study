from art import logo

print(logo)

import random
import os


def clear():
    os.system('cls')


def shuffle():  # 카드 랜덤하게 섞는 함수
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    shuffle_card = random.choice(cards)
    return shuffle_card


def score(final_card):  # 카드 숫자의 합
    # 블랙잭인 경우
    if sum(final_card) == 21 and len(final_card) == 2:
        return 0

    if 11 in final_card and sum(final_card) > 21:
        final_card.remove(11)
        final_card.append(1)
    return sum(final_card)


def versus(player_score, dealer_score):
    if player_score and dealer_score > 21:
        return "패배하였습니다."
    if player_score == dealer_score:
        return "무승부 입니다."
    elif player_score > 21:
        return "패배하였습니다."
    elif dealer_score > 21 > player_score:
        return "승리하였습니다."
    elif player_score > dealer_score:
        return "승리하였습니다."
    elif player_score < dealer_score:
        return "패배하였습니다."

def play():
    player_card = []
    dealer_card = []
    flag = True

    # 카드 받기
    for i in range(2):
        player_card.append(shuffle())
        dealer_card.append(shuffle())

    while flag:
        player_score = score(player_card)
        dealer_score = score(dealer_card)

        print(f"당신의 카드는 {player_card} 입니다. 현재 당신의 점수는 {player_score} 입니다.")
        print((f"딜러의 첫번 째 카드는 {dealer_card[0]} 입니다."))

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            flag = False  # 반복문 종료
        else:
            ask_hit = input("히트(추가로 카드 뽑기)를 하시겠습니까? 하실꺼면 'y', 안하실꺼면 'n'을 입력해주세요: ")
            if ask_hit == "y":
                player_card.append(shuffle())
                #player_score = score(player_card)
            else:
                flag = False
    while dealer_score != 0 and dealer_score <= 16:
        dealer_card.append(shuffle())
        dealer_score = score(dealer_card)

    print(f"플레이어의 최종 카드는 {player_card}이며, 최종 점수는 {player_score} 입니다!")
    print(f"딜러의 최종 카드는 {dealer_card}이며, 최종 점수는 {dealer_score} 입니다!")
    print(versus(player_score, dealer_score))

if input("블랙잭 게임을 시작하실려면 'y'를 입력해주세요! ") == "y":
    play()

while input("블랙잭 게임을 다시 하실꺼면 'y'를 그만 하실꺼면 'n'을 입력해주세요: ") == "y":
    clear()
    play()

print("끝났습니다!")
