import random

# --- Hangman Art Stages (from hangman_art.py) ---
# This list contains ASCII art representations of the hangman stages.
# Each element corresponds to a different number of lives remaining.
hangman_stages = [
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# --- Word List (from hangman_words.py) ---
# This is a list of words that the game will randomly choose from.
word_list = [
    'ardvark', 'baboon', 'camel', 'dinosaur', 'elephant', 'flamingo', 'giraffe',
    'hippopotamus', 'iguana', 'jaguar', 'kangaroo', 'lemur', 'mongoose', 'newt',
    'octopus', 'penguin', 'quokka', 'rhinoceros', 'squirrel', 'tiger', 'unicorn',
    'vulture', 'walrus', 'x-ray', 'yak', 'zebra', 'apple', 'banana', 'cherry',
    'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango',
    'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine',
    'ugli', 'vanilla', 'watermelon', 'zucchini', 'guitar', 'piano', 'trumpet',
    'violin', 'drums', 'flute', 'clarinet', 'saxophone', 'keyboard', 'ukulele',
    'xylophone', 'accordion', 'bagpipes', 'banjo', 'cello', 'harp', 'oboe',
    'piccolo', 'sitar', 'tambourine', 'tuba', 'whistle', 'computer', 'keyboard',
    'mouse', 'monitor', 'printer', 'scanner', 'webcam', 'microphone', 'speaker',
    'router', 'modem', 'server', 'firewall', 'database', 'algorithm', 'software',
    'hardware', 'network', 'internet', 'website', 'browser', 'application', 'program'
]

# --- Game Logic ---

# Choose a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize game variables
end_of_game = False
lives = 6 # Player starts with 6 lives (0-6 stages of hangman_stages)

# Create a blank list to represent the word to be guessed
# Each underscore represents a letter that hasn't been guessed yet.
display = []
for _ in range(word_length):
    display.append("_")

# Keep track of guessed letters to avoid penalizing repeated guesses
guessed_letters = []

# Game loop: continues until the game ends (win or lose)
while not end_of_game:
    # Get a letter guess from the user
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")
        print(f"{' '.join(display)}") # Show current state of the word
        print(hangman_stages[lives]) # Show current hangman stage
        continue # Skip the rest of the loop and ask for another guess

    # Add the current guess to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the chosen word
    # Iterate through each position in the chosen_word
    found_letter = False
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter # If found, update the display list
            found_letter = True

    # If the guessed letter is not in the word, reduce lives
    if not found_letter:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1

    # Print the current state of the word (e.g., "_ a _ _ a _")
    print(f"{' '.join(display)}")

    # Print the current hangman stage based on remaining lives
    print(hangman_stages[lives])

    # Check if the player has won
    # If there are no more underscores in the display, the word has been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Check if the player has lost
    # If lives drop to 0, the game is over.
    if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word was: {chosen_word}")

