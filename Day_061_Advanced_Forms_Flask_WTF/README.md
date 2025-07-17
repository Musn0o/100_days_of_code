# Day_061_Advanced_Forms_Flask_WTF

This project is part of my 100 Days of Code journey.

## Project Description

On Day 61, the focus was on implementing **Advanced Forms** in Flask using the powerful **Flask-WTF** extension. This marked a significant upgrade in handling user input securely and efficiently, covering:

1. **Flask-WTF Integration:** Setting up and configuring Flask-WTF in a Flask application.
    
2. **WTForms Form Creation:** Defining Python classes that represent web forms, including fields (`StringField`, `PasswordField`, `SubmitField`) and their types.
    
3. **Form Validation:** Applying built-in validators (e.g., `DataRequired`, `Length`, `Email`) to ensure user input meets specific criteria before processing.
    
4. **CSRF Protection:** Understanding and implementing Cross-Site Request Forgery (CSRF) protection, a crucial security feature handled automatically by Flask-WTF.
    
5. **Rendering Forms in Templates:** Using Jinja2 to render Flask-WTF forms in HTML templates, including labels, input fields, and error messages.
    
6. **Handling Form Submission (POST):** Processing submitted form data on the server-side, checking for validation errors, and responding accordingly.
    
7. **Flash Messages (Conceptual):** While not explicitly implemented in this minimal example, Flask-WTF often pairs with Flask's `flash` messages for user feedback.
    

This project demonstrates how Flask-WTF simplifies form creation, validation, and security, making web development more robust and secure.

## How to Run

This project requires a specific folder structure:

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_061_Advanced_Forms_Flask_WTF
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install Flask Flask-WTF
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/login`.

- **Initial Page:** You will see a login form with fields for Email and Password.
    
- **Successful Login:** If you enter `admin@email.com` for Email and `12345678` for Password, you will be redirected to a "Success!" page.
    
- **Failed Login (Validation Errors):**
    
    - If you leave fields empty, you'll see "This field is required." errors.
        
    - If you enter an invalid email format, you'll see "Invalid email address."
        
    - If the password is too short, you'll see "Field must be at least 8 characters long."
        
- **Failed Login (Incorrect Credentials):** If you enter valid formats but incorrect credentials, you will be redirected to a "Denied!" page.
    

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Form Handling Best Practices:** Using a dedicated library for forms.
    
- **Server-Side Validation:** Ensuring data integrity and security before processing.
    
- **CSRF Protection:** A fundamental web security measure.
    
- **Separation of Concerns:** Keeping form definitions separate from Flask routes.
    
- **User Feedback:** Providing clear messages for validation errors and login status.
## Author
[Musn0o](https://github.com/Musn0o)