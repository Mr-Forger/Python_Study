import random
import turtle
import os

screen = turtle.Screen()
screen.setup(500, 400)
bet = screen.textinput("거북이 레이스", "어떤 거북이가 경주에서 승리할까요? 색을 선택 해주세요!")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

flag = False

for i in range(0, 6):
    new_t = turtle.Turtle(shape="turtle")
    new_t.penup()
    new_t.color(colors[i])
    new_t.goto(-230, y_positions[i])
    turtles.append(new_t)

if bet:
    flag = True

while flag:
    for turtle in turtles:
        if turtle.xcor() > 230:
            flag = False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"승리하였습니다. {winner}색의 거북이가 승리하였습니다!")
            else:
                print(f"패배하였습니다. {winner}색의 거북이가 승리하였습니다.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)













screen.exitonclick()