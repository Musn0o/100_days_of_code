# Day_011_Blackjack_Capstone_Project

This project is part of my 100 Days of Code journey.

## Project Description

On Day 11, the focus was on developing a command-line **Blackjack (21) Capstone Project**. This comprehensive project allowed me to integrate and apply a wide range of Python concepts, including:

- **Functions:** Structuring the game logic into reusable functions (e.g., dealing cards, calculating scores, comparing hands).
    
- **Lists:** Managing the deck of cards, player's hand, and computer's hand.
    
- **Loops:** Implementing `while` loops for continuous gameplay (player's turn, computer's turn, play again).
    
- **Conditional Statements:** Extensive use of `if`, `elif`, and `else` to handle game rules, win/loss conditions, busts, and Blackjack scenarios.
    
- **Random Module:** Shuffling the deck and dealing random cards.
    
- **Global vs. Local Scope:** Understanding variable scope within functions.
    
- **Recursion (Conceptual):** The `play_game` function can be called recursively to restart the game.
    
- **Clearing the Console:** (Conceptual) Clearing the screen for a cleaner user experience between games.
    

The game simulates a simplified version of Blackjack where the player plays against a computer dealer. The goal is to get as close to 21 as possible without going over.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_011_Blackjack_Capstone_Project
    ```

3. **Run the Python Script:**
    
    ```
    python blackjack_game.py
    ```


## Demo

```
Your cards: [10, 9], current score: 19
Computer's first card: 2
Type 'y' to get another card, type 'n' to pass: n

Your final hand: [10, 9], final score: 19
Computer's final hand: [2, 9, 6], final score: 17
You win 🥳
--------------------------------------------------

Do you want to play a game of Blackjack? Type 'y' or 'n': n
Thanks for playing! 👋
```

## Concepts Learned

- **Complex Game Logic:** Designing and implementing rules for a multi-stage game.
    
- **Function Decomposition:** Breaking down a large problem into smaller, manageable functions.
    
- **List Manipulation for Game State:** Adding, removing, and checking elements in lists to represent game components (cards).
    
- **Handling Edge Cases:** Specifically, managing the Ace card's value (1 or 11) based on the current score.
    
- **User Interface (CLI):** Providing clear prompts and displaying game information effectively in a terminal.
    
## Author

[Musn0o](https://github.com/Musn0o)