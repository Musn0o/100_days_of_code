import turtle
import pandas as pd
import sys
import os

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the map image safely
image_path = "Day_025_US_States_Game/blank_states_img.gif"
if not os.path.exists(image_path):
    print(f"Error: Image file '{image_path}' not found.")
    sys.exit()

screen.addshape(image_path)
turtle.shape(image_path)

# Load the CSV data
try:
    data = pd.read_csv("Day_025_US_States_Game/50_states.csv")
except FileNotFoundError:
    print("Error: '50_states.csv' not found.")
    sys.exit()
except pd.errors.EmptyDataError:
    print("Error: '50_states.csv' is empty.")
    sys.exit()

all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)",
    )

    # User clicked Cancel or closed prompt
    if answer_state is None:
        print("Game stopped by user.")
        break

    answer_state = answer_state.strip().title()

    # User chooses to exit the game early
    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Get coordinates safely using iloc[0]
        state_data = data[data.state == answer_state]
        if not state_data.empty:
            x = int(state_data.iloc[0].x)
            y = int(state_data.iloc[0].y)

            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x, y)
            t.write(answer_state)

# After exiting, save the missing states
missing_states = [state for state in all_states if state not in guessed_states]
if missing_states:
    try:
        pd.DataFrame(missing_states).to_csv(
            "../100_days_of_code/Day_025_US_States_Game/states_to_learn.csv",
            index=False,
        )
        print("List of missing states saved to 'states_to_learn.csv'")
    except Exception as e:
        print(f"Error writing to 'states_to_learn.csv': {e}")
