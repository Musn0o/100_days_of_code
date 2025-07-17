# Day_060_Blog_With_Contact_Form

This project is part of my 100 Days of Code journey.

## Project Description

On Day 60, I enhanced the **Blog Capstone Project** by adding a functional **Contact Form**. This significant addition introduced crucial web development concepts beyond just serving static content:

1. **Handling HTTP POST Requests:** Learning how Flask applications receive and process data submitted via HTML forms.
    
2. **Accessing Form Data (`request.form`):** Retrieving input values from form fields submitted by the user.
    
3. **Email Automation (`smtplib`):** Utilizing Python's built-in `smtplib` library to send emails directly from the Flask application, notifying the blog owner when a new message is received through the contact form.
    
4. **Conditional Rendering:** Displaying different messages or redirecting users based on the success or failure of form submission and email sending.
    
5. **Form Validation (Basic):** (Implicitly) Ensuring all required fields are present before attempting to send an email.
    
6. **Improved User Interaction:** Providing a dedicated contact page with a form for users to send messages.
    

This project demonstrates how to build interactive web applications that can receive user input, process it on the server-side, and trigger actions like sending emails.

## How to Run

1. **Set up Email for Sending:**
    
    - If using Gmail, you'll likely need to generate an "App password" for your account, as direct password login for third-party apps is often blocked for security reasons. (Search "Gmail app password" for instructions).
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_060_Blog_With_Contact_Form
    ```
   
4. **Configure Email Credentials:** Open the `main.py` file and replace the placeholder values for `MY_EMAIL`, `MY_PASSWORD`, and `RECIPIENT_EMAIL` with your actual email details.
    
5. **Install Required Libraries:**
    
    ```
    pip install Flask
    ```
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Home Page (`/`):** The blog home page will be displayed.
    
- **Individual Post Page (`/post/<post_id>`):** Individual blog posts can be viewed.
    
- **Contact Page (`/contact`):** Navigate to `http://127.0.0.1:5000/contact`. You will see a contact form. Fill it out and submit.
    
    - If successful, you will see a "Successfully sent your message!" confirmation on the page.
        
    - An email will be sent to `RECIPIENT_EMAIL` containing the form data.
        

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **HTTP Methods (`GET` vs. `POST`):** Differentiating between requests for retrieving data and submitting data.
    
- **Flask Request Object:** Using `request.method` and `request.form` to handle form submissions.
    
- **Server-Side Form Processing:** How backend code processes user input from forms.
    
- **Email Automation:** Practical application of `smtplib` for sending notifications.
    
- **Security for Credentials:** Importance of using app-specific passwords for email services.
    
- **Dynamic Page Responses:** Changing page content or flow based on user actions.

## Author
[Musn0o](https://github.com/Musn0o)