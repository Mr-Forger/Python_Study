from turtle import Turtle

FONT = ("Consolas", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.scoreboard_update()

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)
