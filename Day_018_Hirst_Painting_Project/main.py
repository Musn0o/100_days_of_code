import turtle
import random
import colorgram

# --- Color Data (Simulating colors extracted from an image) ---
# In a full implementation, you would use a library like 'colorgram' to
# extract colors from a real image. For this exercise, we'll use a predefined
# list of vibrant RGB colors.
# Example using colorgram (not run here):
colors = colorgram.extract('Day_018_Hirst_Painting_Project/image.jpg', 30) # Extract 30 colors from image.jpg
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# --- Turtle Setup ---
# Create a Turtle screen object
screen = turtle.Screen()
# Set the color mode to 255, which allows RGB values from 0-255
screen.colormode(255)
# Create a Turtle object
tim = turtle.Turtle()
# Hide the turtle icon for a cleaner look
tim.hideturtle()
# Set the drawing speed to the fastest possible (0)
tim.speed("fastest")
# Lift the pen up so it doesn't draw when moving to the starting position
tim.penup()

# --- Positioning the Turtle for the Grid ---
# Move the turtle to the starting point for the bottom-left corner of the grid.
# This ensures the painting is somewhat centered or starts from a consistent point.
start_x = -250
start_y = -250
tim.setheading(225) # Point towards bottom-left
tim.forward(300) # Move to a starting position that allows for a centered grid
tim.setheading(0) # Reset heading to east (right)

# --- Drawing the Hirst Painting Grid ---
num_dots_per_row = 10 # Number of dots in each row
num_rows = 10         # Number of rows
dot_size = 20         # Diameter of each dot
spacing = 50          # Distance between the centers of two adjacent dots

# Loop through each row
for row in range(num_rows):
    # Loop through each dot in the current row
    for _ in range(num_dots_per_row):
        # Set the color of the dot to a random RGB color from our list
        tim.dot(dot_size, random.choice(rgb_colors))
        # Move the turtle forward to the position for the next dot in the same row
        tim.forward(spacing)

    # After drawing all dots in a row, move to the beginning of the next row
    tim.backward(spacing * num_dots_per_row) # Move back to the start of the current row
    tim.setheading(90) # Turn north (up)
    tim.forward(spacing) # Move up to the next row's starting y-coordinate
    tim.setheading(0) # Turn back east (right) for the next row

# Keep the window open until it's clicked
screen.exitonclick()
