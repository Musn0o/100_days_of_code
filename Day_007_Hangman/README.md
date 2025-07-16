# Day_007_Hangman

This project is part of my 100 Days of Code journey.

## Project Description

On Day 7, the focus was on building the classic **Hangman game**. This project significantly expanded my understanding and application of:

- **Lists:** Managing the list of words, the display of guessed letters, and the hangman stages.
    
- **Loops:** Using `while` loops to continue the game until it's won or lost, and `for` loops to iterate through words and display.
    
- **Conditional Statements:** Implementing game logic for checking guesses, updating the game state, and determining win/loss conditions.
    
- **String Manipulation:** Handling user input (single letters), replacing underscores with correctly guessed letters, and displaying the current state of the word.
    
- **Random Module:** Selecting a random word for the game.
    
- **ASCII Art:** Incorporating multi-line strings to visually represent the hangman stages, enhancing the user experience.
    

The game challenges the player to guess letters to uncover a hidden word. Each incorrect guess brings the player closer to "hanging," adding a layer of suspense and strategy.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_007_Hangman
    ```

3. **Run the Python Script:**
    
    ```
    python hangman_game.py
    ```

## Demo

```
_ _ _ _ _ _ _ _ _

Guess a letter: a
_ a _ _ _ _ _ _ _

Guess a letter: e
_ a _ _ _ _ _ _ e

Guess a letter: z
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
You guessed z, that's not in the word. You lose a life.
You have 5 lives left.
_ a _ _ _ _ _ _ e

Guess a letter: p
_ a p p _ _ _ _ e

You win.
```

_(Note: The demo shows a partial game. Actual gameplay involves more guesses and hangman stages.)_

## Concepts Learned

- **Game Loop Design:** Structuring a game with continuous play until a condition is met.
    
- **List Comprehension/Manipulation:** Dynamically updating a list (e.g., `display` list).
    
- **Error Handling (Basic):** Checking for invalid inputs or repeated guesses.
    
- **Modularization (Conceptual):** Understanding how different parts of a game (word list, art, game logic) can be separated.
    

## Author

[Musn0o](https://github.com/Musn0o)