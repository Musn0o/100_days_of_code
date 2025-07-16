# --- main.py ---
# This is the main script to run the Snake Game Part 1.
# It sets up the screen and controls the game loop.
from turtle import Screen
import time
from snake import Snake # Import the Snake class from snake.py

# --- Screen Setup ---
screen = Screen()
screen.setup(width=600, height=600) # Set the dimensions of the game window
screen.bgcolor("black") # Set the background color to black
screen.title("My Snake Game") # Set the title of the window
screen.tracer(0) # Turn off screen updates to control animation manually

# Create a Snake object
snake = Snake()

# --- Game Loop ---
game_is_on = True
while game_is_on:
    screen.update() # Update the screen after all segments have moved
    time.sleep(0.1) # Pause for a short duration to control animation speed

    snake.move() # Call the move method of the Snake object

screen.exitonclick() # Keep the window open until clicked


