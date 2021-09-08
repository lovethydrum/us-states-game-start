import turtle
from state_name_generator import Text_generator
import pandas
from scoreboard import Scoreboard

#initiate the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# data[column][index]

data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list
x_cor_list = data["x"].to_list
y_cor_list = data["y"].to_list

scoreboard = Scoreboard()
answer_bank = []

game_active = True
while game_active:
    scoreboard.clear()
    states_remaining = 50 - len(answer_bank)
    scoreboard.write(f"{states_remaining} States Remaining", False, align="center", font=("Arial", 20, "normal"))
    if len(answer_bank) == 50:
        game_active = False
        scoreboard.clear()
        scoreboard.write(f"YOU DID IT!", False, align="center", font=("Arial", 20, "normal"))
    else:
        answer = screen.textinput(title="Guess the State", prompt="Name a state: ").title()
        if answer == "":
            pass
        elif data["state"].str.contains(answer).any():
            if answer in answer_bank:
                pass
            else:
                state_index_value = data[data.state == answer].index.values
                text = Text_generator(int(data["x"][state_index_value]), int(data["y"][state_index_value]), answer)
                answer_bank.append(answer)
screen.exitonclick()
