# --- snake.py ---
# This file defines the Snake class, which manages the snake's segments and movement.

from turtle import Turtle

# Define constants for the starting positions of the snake segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # Distance each segment moves in one step

class Snake:
    def __init__(self):
        self.segments = [] # List to hold all the snake's body segments
        self.create_snake() # Call method to create the initial snake

    def create_snake(self):
        """Creates the initial three segments of the snake."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square") # Create a square-shaped turtle segment
            new_segment.penup() # Lift the pen up so it doesn't draw lines when moving
            new_segment.color("green") # Set the color of the segment
            new_segment.goto(position) # Move the segment to its starting position
            self.segments.append(new_segment) # Add the segment to the list

    def move(self):
        """Moves the snake forward continuously."""
        # Move all segments except the first one to the position of the segment in front of it.
        # This creates the effect of the snake moving as a single unit.
        for seg_num in range(len(self.segments) - 1, 0, -1): # Loop from last segment to second segment
            new_x = self.segments[seg_num - 1].xcor() # Get x-coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor() # Get y-coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y) # Move current segment to that position
        self.segments[0].forward(MOVE_DISTANCE) # Move the head segment forward

