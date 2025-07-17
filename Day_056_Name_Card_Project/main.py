# --- main.py ---
# This file contains the Flask application logic.

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# --- Route 1: Home Page ---
# This route serves the main personal name card page.
@app.route('/')
def home():
    """
    Renders the 'index.html' template, which displays the personal name card.
    """
    return render_template('index.html')

# --- Run the Flask Application ---
# This block ensures the Flask app runs only when the script is executed directly.
# debug=True enables debug mode, which provides helpful error messages and
# automatically reloads the server on code changes.
if __name__ == "__main__":
    app.run(debug=True)

