# Day_055_Higher_Lower_Game_Web_Version

This project is part of my 100 Days of Code journey.

## Project Description

On Day 55, the focus was on building a **web-based "Higher Lower Game"** using the **Flask** framework. This project combined web development concepts with game logic, demonstrating:

1. **Flask Routing:** Defining routes to handle different game states (initial page, guessing results).
    
2. **Dynamic HTML Content:** Returning HTML that changes based on game logic (e.g., displaying "Too High," "Too Low," or "Correct").
    
3. **Path Converters:** Using dynamic URL segments (`<int:guess>`) to capture user input directly from the URL.
    
4. **Random Number Generation:** Generating a secret number for the player to guess.
    
5. **Conditional Logic:** Implementing `if/elif/else` statements to compare the user's guess with the secret number and provide appropriate feedback.
    
6. **HTML Embedding:** Including images directly in the HTML response to enhance the game's visual feedback.
    

The game challenges the player to guess a randomly generated number by navigating to different URLs. The web application provides visual and textual feedback after each guess.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_055_Higher_Lower_Game_Web_Version
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install Flask
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Initial Page:** You will see a welcome message and instructions on how to play.
    
- **Making a Guess:** To make a guess, append a number to the URL, e.g., `http://127.0.0.1:5000/YOUR_GUESS` (replace `YOUR_GUESS` with a number like `50`).
    
- **Feedback:**
    
    - If your guess is too high, the page will display "Too high, try again!" and a corresponding image.
        
    - If your guess is too low, the page will display "Too low, try again!" and a corresponding image.
        
    - If your guess is correct, the page will display "You found me!" and a success image, and prompt you to refresh to play again.
        

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Web-based Game Development:** Building interactive games using a web framework.
    
- **State Management (Simple):** The secret number is generated once per application run.
    
- **Dynamic Content Generation:** Creating HTML responses on the fly based on logic.
    
- **User Interaction via URLs:** A simple method of receiving input from the user through the browser's address bar.
    
- **HTML Embedding:** Including images and styling directly within Flask responses.

## Author

[Musn0o](https://github.com/Musn0o)