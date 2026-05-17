import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()


guessed_answers = []
while len(guessed_answers) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_answers)}/50 States Correct",
                                    prompt="What's another state name?").title()

    if answer_state in all_states and answer_state not in guessed_answers:
        guessed_answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_answers:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
