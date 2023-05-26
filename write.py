from turtle import Turtle


class Write(Turtle):
    def __init__(self, x_cor, y_cor, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(state)
