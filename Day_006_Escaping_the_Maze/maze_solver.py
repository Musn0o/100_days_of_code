# Reeborg's World - Day 6: Escape the Maze
# This code is intended to be run in Reeborg's World (reeborg.ca)
# in the "Maze" challenge.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
