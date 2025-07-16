# Day_012_Number_Guessing_Game

This project is part of my 100 Days of Code journey.

## Project Description

On Day 12, the focus was on building a **Number Guessing Game**. This project helped reinforce concepts related to:

- **Functions:** Structuring the game logic into reusable functions (e.g., `check_answer`, `set_difficulty`).
    
- **Global Constants:** Understanding and using global constants for values that don't change (like the number of turns).
    
- **Loops:** Implementing a `while` loop for the main game flow, allowing the player to keep guessing until they run out of attempts or guess correctly.
    
- **Conditional Statements:** Logic for comparing the user's guess with the secret number and providing feedback.
    
- **Random Module:** Generating a random number for the player to guess.
    
- **User Input:** Taking numerical guesses and difficulty choices from the user.
    

The game challenges the player to guess a randomly generated number within a certain number of attempts, with hints provided after each guess.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_012_Number_Guessing_Game
    ```


3. **Run the Python Script:**
    
    ```
    python number_guessing_game.py
    ```


## Demo

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
You have 8 attempts remaining to guess the number.
Make a guess: 37
Too high.
You have 7 attempts remaining to guess the number.
Make a guess: 30
You got it! The answer was 30.
```

## Concepts Learned

- **Game Loop Design:** Creating an interactive game loop with clear win/loss conditions.
    
- **Managing Attempts:** Decrementing a counter and ending the game when attempts run out.
    
- **Providing Feedback:** Giving hints (too high/too low) to guide the player.
    
- **Function Parameters and Return Values:** Passing data between different parts of the program.
    

## Author

[Musn0o](https://github.com/Musn0o)