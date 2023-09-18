################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") #함수 내부의 enemies = 2 출력 <= 지역 변수이기 때문에 함수 내부에서만 쓰인다.

increase_enemies()
print(f"enemies outside function: {enemies}") #외부의 enemies = 1 출력 <= 전역 변수라 먼저 쓰인다.

#지역 변수는 정해진 범위에서만 사용가능하고, 전역 변수는 어디에서나 쓸 수 있다.