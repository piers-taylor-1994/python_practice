import pandas
import turtle

screen = turtle.Screen()
screen.screensize(200, 200)
screen.title("U.S. States Game")
image = "Day_25/us_map/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

with open("Day_25/us_map/50_states.csv") as file:
    data = pandas.read_csv(file)

states = data["state"].to_list()
test = data[data["state"] == "Colorado"]
guessed_states = []

while len(guessed_states) < 50:
    title = "Guess the state"
    if len(guessed_states) > 0:
        title = f"{len(guessed_states)}/50 states correct"
    answer = screen.textinput(title, "What's another state's name?")

    if answer in states:
        state = data[data.state == answer]
        t = turtle.Turtle(visible=False)
        t.penup()
        t.clear()
        t.speed("fastest")
        t.goto(state.x.item(), state.y.item())
        t.write(state.state.item())

    if answer == "Exit":
        missing_states = [s for s in states if s not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day_25/us_map/states_to_learn.csv")
        break