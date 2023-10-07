import turtle
import os

t = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def rotate_clockwise():
    t.right(10)


def rotate_counter_clockwise():
    t.left(10)


def clear():
    t.reset()


screen.listen()  # 이 메소드가 시작하면 이벤트에 바인딩 시켜야한다.
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
