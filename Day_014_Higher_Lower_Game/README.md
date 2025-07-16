# Day_014_Higher_Lower_Game

This project is part of my 100 Days of Code journey.

## Project Description

On Day 14, the focus was on building the **Higher Lower Game**, a fun command-line game that pits your intuition against celebrity follower counts. This project provided an excellent opportunity to apply and reinforce:

- **Dictionaries within Lists:** Storing structured data (name, follower count, description) for multiple entities.
    
- **Random Module:** Selecting random and distinct accounts for comparison.
    
- **Functions:** Modularizing code into functions for clarity and reusability (e.g., `get_random_account`, `format_data`, `check_answer`).
    
- **Loops:** Implementing a `while` loop to keep the game running as long as the user guesses correctly.
    
- **Conditional Statements:** Logic for comparing follower counts, determining correctness of guess, and handling game over conditions.
    
- **Score Tracking:** Maintaining and displaying the user's score.
    
- **Clearing the Console:** (Conceptual) Clearing the screen between rounds for a cleaner game experience.
    

The game presents two accounts (e.g., celebrities, brands) and asks the user to guess which one has more followers. A correct guess increases the score and continues the game; an incorrect guess ends it.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_014_Higher_Lower_Game
    ```

3. **Run the Python Script:**
    
    ```
    python higher_lower_game.py
    ```


## Demo

```
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.
    vs.
Against B: Selena Gomez, a Musician, from United States.
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1
Compare A: Selena Gomez, a Musician, from United States.
    vs.
Against B: Ariana Grande, a Musician, from United States.
Who has more followers? Type 'A' or 'B': B
You're right! Current score: 2
Compare A: Ariana Grande, a Musician, from United States.
    vs.
Against B: Dwayne "The Rock" Johnson, a Actor, from United States.
Who has more followers? Type 'A' or 'B': A
Sorry, that's wrong. Final score: 2
```

## Concepts Learned

- **Data Structures:** Using lists of dictionaries to manage complex data.
    
- **Game Loop with State Management:** Designing a game that progresses through rounds and maintains score.
    
- **Random Selection with Constraints:** Ensuring distinct choices for comparison.
    
- **Clear User Feedback:** Providing immediate feedback on guesses and scores.
    
- **Modular Code:** Breaking down complex game logic into smaller, testable functions.
    
## Author

[Musn0o](https://github.com/Musn0o)