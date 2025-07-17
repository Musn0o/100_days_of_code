# --- main.py ---
# This file contains a basic Flask web application.

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# --- Route 1: Home Page ---
# The '@app.route("/")' decorator defines a route for the root URL ("/").
# When a user accesses this URL, the function immediately below it will be executed.
@app.route("/")
def hello_world():
    """
    Returns a simple 'Hello, World!' message when the root URL is accessed.
    """
    return "<p>Hello, World!</p>"

# --- Route 2: /bye Page ---
# Defines a route for the "/bye" URL.
@app.route("/bye")
def bye():
    """
    Returns a 'Bye!' message when the /bye URL is accessed.
    """
    return "<h1>Bye!</h1>"

# --- Route 3: Dynamic Path with Variable ---
# Defines a route that can take a variable part in the URL.
# '<name>' is a path converter, capturing whatever is in that part of the URL
# and passing it as an argument to the function.
@app.route("/username/<name>")
def greet_user(name):
    """
    Returns a personalized greeting using the 'name' provided in the URL.
    Example: Accessing /username/Angela will display "Hello, Angela!"
    """
    return f"Hello, {name}!"

# --- Route 4: Dynamic Path with Multiple Variables and Type Conversion ---
# Defines a route that takes a name (string) and a number (integer).
# '<path:name>' allows 'name' to include slashes.
# '<int:number>' converts the 'number' part of the URL to an integer.
@app.route("/<name>/<int:number>")
def greet_name_and_number(name, number):
    """
    Returns a message combining a name and a number from the URL.
    Example: Accessing /John/123 will display "Hello John, your number is 123."
    """
    return f"Hello {name}, your number is {number}."


# --- Run the Flask Application ---
# This block ensures the Flask app runs only when the script is executed directly.
# debug=True enables debug mode, which provides helpful error messages and
# automatically reloads the server on code changes.
if __name__ == "__main__":
    app.run(debug=True)

