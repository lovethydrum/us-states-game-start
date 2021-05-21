from turtle import Turtle

class Text_generator(Turtle):
    def __init__(self, xcor, ycor, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(xcor, ycor)
        self.write(state, False, align="center")