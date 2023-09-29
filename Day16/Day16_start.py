import turtle
import another_module

print(another_module.another_variable)

t = turtle.Turtle() # t: 객체, Turtle(): 클래스
print(t)
t.shape("turtle")
t.color("blue")
t.forward(100)

my_screen = turtle.Screen()
print(my_screen.canvheight) #객체 이름.속성
my_screen.exitonclick()
