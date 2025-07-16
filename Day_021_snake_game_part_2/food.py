# --- food.py ---
# This file defines the Food class, inheriting from Turtle.

from turtle import Turtle
import random

class Food(Turtle): # Food class inherits from Turtle
    def __init__(self):
        super().__init__() # Call the constructor of the parent class (Turtle)
        self.shape("circle") # Set the shape of the food to a circle
        self.penup() # Lift the pen up
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # Make the circle smaller (10x10 pixels)
        self.color("red") # Set the color of the food
        self.speed("fastest") # Set drawing speed to fastest
        self.refresh() # Place the food at a random initial location

    def refresh(self):
        """Moves the food to a new random location on the screen."""
        random_x = random.randint(-280, 280) # Random x-coordinate within screen bounds
        random_y = random.randint(-280, 280) # Random y-coordinate within screen bounds
        self.goto(random_x, random_y) # Move food to the new random position


