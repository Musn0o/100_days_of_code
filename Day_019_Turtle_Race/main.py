from turtle import Turtle, Screen
import random

# --- Screen Setup ---
screen = Screen()
screen.setup(width=500, height=400) # Set the dimensions of the screen

# Get user's bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Starting Y-coordinates for each turtle to be lined up
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = [] # List to store all turtle objects

# --- Create and Position Turtles ---
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle") # Create a new turtle object with a turtle shape
    new_turtle.penup() # Lift the pen up so it doesn't draw when moving to starting position
    new_turtle.color(colors[turtle_index]) # Set the color of the turtle
    new_turtle.goto(x=-230, y=y_positions[turtle_index]) # Move to the starting line
    all_turtles.append(new_turtle) # Add the new turtle to the list

# --- Race Logic ---
is_race_on = False

# Only start the race if the user has placed a bet
if user_bet:
    is_race_on = True

winning_color = "" # Variable to store the color of the winning turtle

while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line (x-coordinate > 230)
        if turtle.xcor() > 230:
            is_race_on = False # End the race
            winning_color = turtle.pencolor() # Get the color of the winning turtle
            # Check if the user's bet matches the winning color
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break # Exit the inner loop once a winner is found

        # Move each turtle forward by a random amount
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick() # Keep the window open until clicked
