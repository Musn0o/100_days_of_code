# Day_008_Caesar_Cipher

This project is part of my 100 Days of Code journey.

## Project Description

On Day 8, the focus was on building a **Caesar Cipher** encryption/decryption tool. This project provided a practical application for understanding and utilizing:

- **Functions with Parameters:** Defining and calling functions that accept multiple arguments to perform specific tasks (e.g., `encrypt` and `decrypt` or a combined `caesar` function).
    
- **Keyword Arguments:** (If implemented) Understanding how to pass arguments using keywords for clarity.
    
- **Loops:** Iterating through strings to process each character.
    
- **Conditional Statements:** Handling different types of characters (letters vs. non-letters) and determining whether to encrypt or decrypt.
    
- **Modulo Operator (`%`):** Using the modulo operator to wrap around the alphabet when shifting letters, ensuring the shift stays within the bounds of 'a' through 'z' or 'A' through 'Z'.
    
- **User Interaction Loop:** Implementing a `while` loop to allow the user to run the cipher multiple times until they choose to exit.
    

The application takes a message and a shift amount, then encrypts or decrypts the message using the Caesar cipher algorithm.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_008_Caesar_Cipher
    ```

3. **Run the Python Script:**
    
    ```
    python caesar_cipher.py
    ```


## Demo

```
  _ __  _ __
 | '_ \\| '_ \\
 | |_) | |_) |
 | .__/| .__/
 |_|   |_|

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
5
Here's the encoded result: mjqqt btwqi
Type 'yes' if you want to go again. Otherwise type 'no'.
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
mjqqt btwqi
Type the shift number:
5
Here's the decoded result: hello world
Type 'yes' if you want to go again. Otherwise type 'no'.
no
Goodbye!
```

## Concepts Learned

- **Function Definition and Calling:** Structuring code into reusable blocks.
    
- **Alphabet Manipulation:** Handling character positions within a defined alphabet.
    
- **Algorithmic Thinking:** Breaking down a problem (encryption/decryption) into logical steps.
    
- **Robust Input Handling:** Ensuring the program can handle various user inputs and continue or terminate as requested.
    

## Author

[Musn0o](https://github.com/Musn0o)