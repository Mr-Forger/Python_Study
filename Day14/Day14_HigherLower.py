import random
import os
from art import logo, vs
from game_data import data


def clear():
    os.system('cls')


print(logo)


def select_celebrity():
    return random.choice(data)


def celebrity_info(information):
    name = information["name"]
    description = information["description"]
    country = information["country"]

    return f"이름: {name}, 직업: {description}, 국적: {country}"


def compare(choose, a_follower, b_follower):
    if a_follower > b_follower:
        return choose == "a"  # choose와 입력한 값(a)가 같은지 확인하고 반환한다
    else:
        return choose == "b"


def play():
    flag = True
    score = 0
    celeb_a = select_celebrity()
    celeb_b = select_celebrity()

    while flag:
        print(f"A: {celebrity_info(celeb_a)}.")
        print(vs)
        print(f"B: {celebrity_info(celeb_b)}.")

        while celeb_a == celeb_b:
            celeb_b = select_celebrity()

        choose = input("A와 B중 누가 더 팔로워 수가 많은 것 같나요?: ").lower()
        a_follower = celeb_a["follower_count"]
        b_follower = celeb_b["follower_count"]
        versus = compare(choose, a_follower, b_follower)

        if versus:
            score += 1
            print(f"맞췄습니다! 현재스코어는 {score}입니다!\n 다음 단계로 넘어가겠습니다!\n")
            celeb_a = celeb_b
            celeb_b = select_celebrity()
        else:
            flag = False
            print(f"틀렸습니다! 당신의 최종 스코어는 {score}입니다!\n")


play()

# Chat GPT의 솔루션과의 비교
# 두 코드는 동일한 목적을 위해 작성되었습니다: 유저에게 두 명의 유명인의 팔로워 수를 비교하도록 하고, 누가 더 많은 팔로워를 가지고 있는지 추측하게 합니다. 그러나 몇 가지 주요 차이점과 코드의 효율성에 영향을 줄 수 있는 요소들이 있습니다.
#
# 명명 규칙:
# 첫 번째 코드는 영어로 작성되었으며, 두 번째 코드는 일부 한국어로 작성되었습니다. 이것은 효율성에 직접적인 영향을 주지 않지만 코드의 가독성과 유지 보수에 영향을 줄 수 있습니다.

# 중복 코드:
# 두 코드 모두 celeb_a와 celeb_b가 동일할 때 새로운 유명인을 선택하도록 하는 로직을 포함하고 있습니다. 그러나 첫 번째 코드에서는 게임의 각 반복마다 이를 확인하는 반면, 두 번째 코드에서는 사용자의 입력 이전에 이를 확인합니다. 이는 두 번째 코드가 약간 더 효율적일 수 있음을 의미합니다.

# 코드 구조:
# 두 코드는 모두 기능별로 함수를 잘 분리하였습니다. 이로 인해 코드의 유지 보수가 용이하며 가독성이 향상됩니다.

# clear 함수:
# 첫 번째 코드는 replit 라이브러리의 clear 함수를 사용하여 화면을 지우고, 두 번째 코드는 os 라이브러리의 cls 명령어를 사용하여 화면을 지웁니다. replit의 clear 함수는 replit.com 플랫폼에서만 작동하기 때문에, 다른 환경에서 코드를 실행하려면 두 번째 코드의 접근 방식이 더 좋습니다.

# 피드백 메시지:
# 두 코드는 사용자가 정답을 맞추거나 틀렸을 때 다른 피드백 메시지를 제공합니다. 이는 주관적인 차이이며 효율성과는 관련이 없습니다.

# 결론적으로, 두 코드 모두 유사한 방식으로 작동하며 큰 성능 차이는 없습니다. 그러나 일반적인 환경에서의 호환성을 고려한다면 두 번째 코드의 접근 방식이 조금 더 우수하다고 볼 수 있습니다.
