import turtle
import pandas
from score_board import Scoreboard


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = turtle.Turtle()
state.hideturtle()
#score = Scoreboard()


data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
correct_guess_list = []

while len(correct_guess_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess_list)}/50 States Correct", prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_guess_list]
        # missing_states = []
        # for state in correct_guess_list:
        #     if state not in correct_guess_list:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
    if answer_state in state_list:
        correct_guess_list.append(answer_state)
        st_name = data[data.state == answer_state]
        state.penup()
        state.goto(int(st_name.x), int(st_name.y))
        state.write(answer_state)


diff1 = set(state_list) - set(correct_guess_list)
# data_new = pandas.DataFrame(diff1)
# data_new.to_csv("states_to_learn.csv")
        #
        # score.increase_score()
        # score.update_scoreboard()