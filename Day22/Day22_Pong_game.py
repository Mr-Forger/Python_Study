from turtle import Screen, Turtle
from Day22.paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.scoreboard_update()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

flag = True
while flag:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # 벽에 부딫혔을때 튕겨지게 하는 조건
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # 패들에 부딫혔을때 마찬가지로 튕겨지게 하는 조건
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # 패들을 놓쳤을때 초기화 시키는 조건
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_scoring()

    if ball.xcor() < -380:
        ball.reset_position()  # 해당 함수에서 포지션 x_bounce 메소드만 호출하는데 왜 반대방향으로 갈까 -> x *= -1을 통해 양수 음수를 계속 바꾸기 때문
        scoreboard.r_scoring()

screen.exitonclick()
