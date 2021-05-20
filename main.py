import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the State", prompt="Name a state: ").capitalize()

data = pandas.read_csv("50_states.csv")
if data[data.state == answer_state]:
    turtle.write(answer_state, False, align="center")

screen.exitonclick()
