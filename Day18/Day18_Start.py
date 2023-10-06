import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)

# #랜덤으로 뻗게하기
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]
# t.pensize(15)
t.speed("fastest")
# for _ in range(200):
#     t.color(random_color())
#     t.forward(30)
#     t.setheading(random.choice(directions))

# 작은 원과 큰 원
n = 5
for i in range(int(360/n)):
    t.color(random_color())
    t.circle(100)
    t.setheading(t.heading() + n)


screen = turtle.Screen()
screen.exitonclick()
