# --- main.py ---
# This file contains the Flask web application for the Higher Lower Game.

from flask import Flask
import random

# Create a Flask application instance
app = Flask(__name__)

# Generate a random number between 0 and 9 for the game.
# This number will remain constant for the duration the Flask app is running.
SECRET_NUMBER = random.randint(0, 9)
print(f"Secret number is: {SECRET_NUMBER}") # For debugging purposes

# --- Route 1: Home Page ---
# This route serves the initial game instructions and the main prompt.
@app.route('/')
def home_page():
    """
    Renders the home page of the game, instructing the user to guess a number.
    """
    return ("<h1>Guess a number between 0 and 9!</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPYw230oXwK0g/giphy.gif' width='400px'>"
            "<p>To play, append your guess to the URL, e.g., /5</p>")

# --- Route 2: Guessing Logic ---
# This route handles the user's guess, which is passed as an integer in the URL path.
@app.route('/<int:guess>')
def check_guess(guess):
    """
    Checks the user's guess against the SECRET_NUMBER and provides feedback.
    Displays different messages and GIFs based on the correctness of the guess.
    """
    if guess > SECRET_NUMBER:
        return ("<h1 style='color: red'>Too high, try again!</h1>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='400px'>")
    elif guess < SECRET_NUMBER:
        return ("<h1 style='color: blue'>Too low, try again!</h1>"
                "<img src='https://media.giphy.com/media/l0HlCqV3gYq3y/giphy.gif' width='400px'>")
    else:
        return ("<h1 style='color: green'>You found me!</h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmTEzBq8/giphy.gif' width='400px'>"
                "<p>Refresh the page to play again!</p>")

# --- Run the Flask Application ---
# This block ensures the Flask app runs only when the script is executed directly.
# debug=True enables debug mode, which provides helpful error messages and
# automatically reloads the server on code changes.
if __name__ == "__main__":
    app.run(debug=True)

