import random

# ASCII art for Rock, Paper, and Scissors
# These multi-line strings are used to visually represent the choices in the game.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# A list to easily access the ASCII art based on numerical choice (0=Rock, 1=Paper, 2=Scissors)
game_images = [rock, paper, scissors]

# Get user's choice
# The input is converted to an integer.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate user input
# If the user enters a number outside the valid range (0, 1, 2), they lose immediately.
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    # Display the user's choice using the corresponding ASCII art
    print("You chose:")
    print(game_images[user_choice])

    # Generate a random choice for the computer
    # random.randint(0, 2) ensures the computer's choice is also 0, 1, or 2.
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Determine the winner based on game rules
    # Rock (0) beats Scissors (2)
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    # Scissors (2) beats Rock (0) - computer wins
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    # If computer's choice is numerically greater (e.g., Paper(1) vs Rock(0), Scissors(2) vs Paper(1))
    # and it's not the special Rock-Scissors case, computer wins.
    elif computer_choice > user_choice:
        print("You lose")
    # If user's choice is numerically greater (e.g., Paper(1) vs Rock(0), Scissors(2) vs Paper(1))
    # and it's not the special Rock-Scissors case, user wins.
    elif user_choice > computer_choice:
        print("You win!")
    # If both choices are the same, it's a draw.
    elif computer_choice == user_choice:
        print("It's a draw")

