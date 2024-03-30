import turtle
import pandas
from mapwritter import MapWritter
IMAGE = "./blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=700, height=500)
screen.addshape(IMAGE)
turtle.Turtle(shape=IMAGE)

states_data = pandas.read_csv("./50_states.csv")
all_states = states_data.state.to_list()

map_writter = MapWritter()
guessed_states = []
score = 0
while len(all_states) > 0:
    try:
        user_guess = screen.textinput(title=f"{score}/50 Guess the State", prompt="Type the name of any state:").title()

        if user_guess == "Exit":
            missing_states = [state for state in all_states if state not in guessed_states]
            new_data = pandas.DataFrame({"state": missing_states})
            new_data.to_csv("./missed_states.csv")
            break

        if user_guess in all_states:
            state = states_data[states_data.state == user_guess].values[0]
            guessed_states.append(user_guess)

            map_writter.write_answer(name=user_guess, position=(state[1], state[2]))
            score += 1

    # Closes the game without any error
    except AttributeError:
        break
