# Day_010_Calculator

This project is part of my 100 Days of Code journey.

## Project Description

On Day 10, the focus was on building a **Command-Line Calculator**. This project provided a comprehensive application for understanding and utilizing:

- **Functions with Return Values:** Defining functions for basic arithmetic operations (add, subtract, multiply, divide) that return their results.
    
- **Dictionaries:** Using dictionaries to store and retrieve functions based on operation symbols, making the code more organized and extensible.
    
- **Loops:** Implementing a `while` loop to allow for continuous calculations (e.g., taking the result of one operation as the first number for the next).
    
- **Recursion (Conceptual / Iterative Loop):** Designing the program to allow the user to continue calculating with the previous result or start a new calculation.
    
- **User Input:** Taking numerical inputs and operation symbols from the user.
    
- **Conditional Statements:** Handling different operations and user choices (continue, new calculation, exit).
    

The calculator allows users to perform sequential arithmetic operations, building on previous results, or start fresh with a new calculation.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_010_Calculator
    ```

3. **Run the Python Script:**
    
    ```
    python calculator.py
    ```


## Demo

```
  _ __ __ _ _ __   __ _  ___ _ __
 | '__/ _` | '_ \ / _` |/ _ \ '__|
 | | | (_| | | | | (_| |  __/ |
 |_|  \__,_|_| |_|\__, |\___|_|
                  |___/

What's the first number?: 10
+
-
*
/
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or 'n' to start a new calculation, or 'x' to exit: y
Pick an operation: *
What's the next number?: 2
15.0 * 2.0 = 30.0
Type 'y' to continue calculating with 30.0, or 'n' to start a new calculation, or 'x' to exit: n
What's the first number?: 7
+
-
*
/
Pick an operation: -
What's the next number?: 3
7.0 - 3.0 = 4.0
Type 'y' to continue calculating with 4.0, or 'n' to start a new calculation, or 'x' to exit: x
Goodbye!
```

## Concepts Learned

- **Functions as First-Class Objects:** Storing functions in dictionaries and calling them dynamically.
    
- **Modular Programming:** Breaking down the calculator into smaller, manageable functions.
    
- **Program Looping for User Interaction:** Creating an interactive loop for continuous operation.
    
- **Handling Floating-Point Numbers:** Performing calculations with decimals.
    
## Author

[Musn0o](https://github.com/Musn0o)