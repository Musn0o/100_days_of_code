import random

# Define global constants for the number of turns in each difficulty
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer.
# Returns the number of turns remaining.
def check_answer(guess, answer, turns):
  """Checks guess against answer. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1 # Decrease turns if guess is too high
  elif guess < answer:
    print("Too low.")
    return turns - 1 # Decrease turns if guess is too low
  else:
    print(f"You got it! The answer was {answer}.")
    return turns # If correct, turns don't change (game effectively ends)

# Function to set the difficulty level and return the corresponding number of turns.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

# Main game function
def game():
  # Print welcome message
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  # Generate a random number between 1 and 100 (inclusive)
  answer = random.randint(1, 100)

  # Set the number of turns based on difficulty chosen by the user
  turns = set_difficulty()

  guess = 0 # Initialize guess to a value that won't match the answer initially

  # Game loop: continues as long as the guess is not correct and turns are remaining
  while guess != answer and turns > 0:
    print(f"You have {turns} attempts remaining to guess the number.")

    # Get the user's guess
    guess = int(input("Make a guess: "))

    # Check the guess and update turns
    turns = check_answer(guess, answer, turns)

    # If turns run out and the guess is still not correct, inform the user
    if turns == 0 and guess != answer:
      print("You've run out of guesses, you lose.")
      print(f"The answer was {answer}.")

# Start the game
game()
