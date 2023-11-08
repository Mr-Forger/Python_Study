import turtle
import pandas

screen = turtle.Screen()
screen.title("State Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"Your State Correct: {len(guess_state)}/50", prompt="Enter the State Name!").title()
    print(answer_state)

    # 1. 입력한 주가 csv 파일에 있는 주인지 확인하기, 맞으면 해당 x, y좌표에 맞게 텍스트를 위치시켜야한다.
    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

turtle.mainloop()
