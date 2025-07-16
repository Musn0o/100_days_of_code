import random
import os # Used for clearing the console

# Data for the game (list of dictionaries)
# Each dictionary represents an account with its name, follower_count, description, and country.
data = [
    {
        'name': 'Instagram',
        'follower_count': 650,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 600,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 480,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 420,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 390,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Dwayne "The Rock" Johnson',
        'follower_count': 380,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 370,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 360,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 310,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 270,
        'description': 'Musician',
        'country': 'United States'
    }
]

# Higher Lower Game ASCII Art Logo (simplified, no complex logo as per request)
# You can imagine a simple text-based logo here if desired, or just start with text.
# print("Higher Lower Game")

# Function to get a random account from the data list.
def get_random_account():
  """Returns a random account from the data list."""
  return random.choice(data)

# Function to format the account data into a readable string for display.
def format_data(account):
  """Takes the account data and returns the printable format."""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}."

# Function to check if the user's guess is correct.
# It compares the follower counts of account A and account B.
def check_answer(guess, a_followers, b_followers):
  """
  Checks if the user's guess is correct based on follower counts.
  Returns True if correct, False otherwise.
  """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Main game function
def game():
  score = 0
  game_should_continue = True
  # Get initial two distinct accounts.
  account_a = get_random_account()
  account_b = get_random_account()

  # Ensure account_a and account_b are different.
  while account_a == account_b:
    account_b = get_random_account()

  # Game loop: continues as long as the user guesses correctly.
  while game_should_continue:
    # Set account_a to be the previous account_b if the game continues.
    # This makes the game flow smoothly from one comparison to the next.
    account_a = account_b
    account_b = get_random_account()

    # Ensure account_a and account_b are different after the shift.
    while account_a == account_b:
      account_b = get_random_account()

    # Display comparison information to the user.
    print(f"Compare A: {format_data(account_a)}")
    print("    vs.")
    print(f"Against B: {format_data(account_b)}")

    # Get user's guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts for comparison.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check the user's answer.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the console for the next round.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Provide feedback and update score.
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

# Start the game.
game()
