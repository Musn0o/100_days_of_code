# Day_054_Web_Dev_Intro_With_Flask

This project is part of my 100 Days of Code journey.

## Project Description

On Day 54, the focus shifted to **Web Development** with an introduction to **Flask**, a lightweight Python web framework. This day covered the fundamental concepts required to build and run a basic web application:

1. **Flask Setup:** Installing Flask and setting up a minimal Flask application.
    
2. **Routing:** Defining different URL paths (routes) for the web application using the `@app.route()` decorator.
    
3. **Returning HTML:** Sending simple HTML content back to the user's browser when a specific route is accessed.
    
4. **Running a Flask App:** Understanding how to start the Flask development server to make the web application accessible locally.
    
5. **Basic Web Server Functionality:** Grasping the client-server model in the context of web requests.
    

This project serves as a foundational step into backend web development, demonstrating how Python can be used to serve web content.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_054_Web_Dev_Intro_With_Flask
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

- Visiting `http://127.0.0.1:5000/` will display "Hello, World!"
    
- Visiting `http://127.0.0.1:5000/bye` will display "Bye!"
    
- Visiting `http://127.0.0.1:5000/username/YOUR_NAME` (replace `YOUR_NAME` with any name) will display a personalized greeting, e.g., "Hello, YOUR_NAME!"
    

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Web Frameworks:** Introduction to what a web framework is and its purpose.
    
- **HTTP Basics:** Understanding simple GET requests.
    
- **Routing:** Mapping URLs to specific Python functions.
    
- **Function Decorators:** Using `@app.route` to assign URLs to functions.
    
- **Dynamic URLs:** Creating routes that can accept variable parts (path converters).
    
- **Local Development Server:** Running a web application on your local machine.

## Author

[Musn0o](https://github.com/Musn0o)