import turtle

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.color("red")

#정사각형 만들기
for i in range(4):
    t.forward(100)
    t.left(90)


screen.exitonclick()