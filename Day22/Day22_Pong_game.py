from turtle import Screen, Turtle
from Day22.paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

flag = True
while flag:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #벽에 부딫혔을때
    if ball.ycor() > 280 or ball.ycor() < -280:
        #튕겨져야댐
        ball.bounce()

screen.exitonclick()