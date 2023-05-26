import turtle
import pandas
from tkinter import messagebox
from write import Write

screen = turtle.Screen()
screen.title('U.S State Game')
image = 'blank_states_img.gif'
screen.addshape(image)


turtle.shape('blank_states_img.gif')
data = pandas.read_csv('50_states.csv')


guess = []
count = 0
state_list = data.state.tolist()
state_length = len(state_list)
state_condition = False
game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{len(guess)}/{state_length} Guess the state",
                                    prompt="What's another state's name").title()
    for state in state_list:
        if answer_state == state:
            state_condition = True
            break
        else:
            state_condition = False

    if state_condition:
        if answer_state not in guess:
            correct_answer = data[data.state == answer_state]
            x_cor = int(correct_answer.x.iloc[0])
            y_cor = int(correct_answer.y.iloc[0])
            state = str(correct_answer.state.iloc[0])
            turtle = Write(x_cor, y_cor, state)
            guess.append(state)
        else:
            messagebox.showerror('ERROR', 'Already listed')

    elif answer_state == 'Exit':
        states_not_listed = []
        for state in state_list:
            if state not in guess:
                states_not_listed.append(state)

        states_not_listed = pandas.DataFrame(states_not_listed)
        states_not_listed.to_csv('states_not_listed.csv')
        break

    else:
        messagebox.showerror('ERROR', 'Wrong state')
