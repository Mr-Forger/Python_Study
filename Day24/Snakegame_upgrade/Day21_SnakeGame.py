import turtle
import time

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

flag = True

while flag:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #먹이를 먹었을 경우 뱀의 꼬리가 늘어나게 만들기
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #벽에 충돌 했을 경우 게임이 끝나게 하기
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        flag = False
        scoreboard.game_over()

    #머리가 자기의 꼬리에 부딫혔을때 게임이 끝나게 하기
    for segment in snake.segments[1:]: #슬라이싱을 통해 머리부분인 인덱스0번 부터가 아닌 1번 인덱스부터 for문이 돌도록 설정.
        if snake.head.distance(segment) < 10:
            flag = False
            scoreboard.game_over()
















screen.exitonclick()