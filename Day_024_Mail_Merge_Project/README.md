# Day_024_Mail_Merge_Project

This project is part of my 100 Days of Code journey.

## Project Description

On Day 24, I created a **Mail Merge** tool that automates the process of personalizing letters. This project demonstrates how to read from and write to files, and how to manipulate strings to replace placeholders with actual data.

- **Read Names:** The program reads a list of names from a file.
- **Read Letter Template:** It reads a letter template with a placeholder for the name.
- **Generate Personalized Letters:** For each name, it replaces the placeholder in the letter with the actual name and saves the personalized letter in a separate file.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_024_Mail_Merge_Project
    ```

3. **Prepare Input Files:**
    - Place the letter template in the `Input/Letters/starting_letter.txt` file.
    - Add the names to the `Input/Names/invited_names.txt` file, one name per line.

4. **Run the Main Python Script:**
    
    ```
    python main.py
    ```

5. **Check the Output:**
    - The personalized letters will be saved in the `Output/ReadyToSend` directory.

## Concepts Learned

- **File I/O:** Reading from and writing to files.
- **String Manipulation:** Using the `replace()` method to substitute placeholders.
- **File Paths:** Working with relative file paths to organize input and output files.
- **Automation:** Automating a repetitive task to save time and reduce errors.

## Author

[Musn0o](https://github.com/Musn0o)
