# Day_032_Birthday_Wisher

This project is part of my 100 Days of Code journey.

## Project Description

On Day 32, I built an automated **Birthday Wisher** that sends personalized birthday emails. This project demonstrates how to use Python to send emails, work with dates, and generate random letters.

- **Email Automation:** Sends emails using Python's `smtplib`.
- **Date Handling:** Uses the `datetime` module to check the current date against birthdays.
- **Data Management:** Reads birthday data from a CSV file.
- **Personalized Letters:** Generates random birthday messages from a collection of templates.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_032_Birthday_Wisher
    ```

3. **Prepare Input Files:**
    - Create a `birthdays.csv` file in the project directory with the following columns: `name`, `email`, `year`, `month`, `day`.
    - Create a `letter_templates` directory and place your letter templates (e.g., `letter_1.txt`, `letter_2.txt`) inside it. Use `[NAME]` as a placeholder for the recipient's name.

4. **Configure Email Credentials:**
    - Open `main.py` and replace `YOUR_EMAIL` and `YOUR_PASSWORD` with your actual email address and app password (if using Gmail, you'll need to generate an app password).

5. **Run the Main Python Script:**
    
    ```
    python main.py
    ```

## Demo

When you run the script, it will check if today is anyone's birthday listed in `birthdays.csv`. If it is, a personalized birthday email will be sent to that person using a randomly selected letter template.

## Concepts Learned

- **`smtplib`:** Sending emails programmatically.
- **`datetime` module:** Working with dates and times.
- **`pandas`:** Reading data from CSV files.
- **File I/O:** Reading and manipulating text files.
- **Randomization:** Selecting random elements from a list.

## Author

[Musn0o](https://github.com/Musn0o)
