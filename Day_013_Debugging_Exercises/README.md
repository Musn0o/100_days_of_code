# Day_013_Debugging_Exercises

This project is part of my 100 Days of Code journey.

## Project Description

Day 13 was dedicated to **debugging**, a crucial skill for any programmer. Instead of building a new application from scratch, this day involved identifying and fixing errors in pre-existing code snippets. The exercises focused on common pitfalls and logical errors, providing hands-on experience in tracing code execution and understanding error messages.

The debugging challenges covered:

1. **Odd or Even Checker:** Fixing a program to correctly identify if a number is odd or even.
    
2. **Leap Year Checker:** Correcting logic to accurately determine if a given year is a leap year.
    
3. **FizzBuzz Game:** Debugging the classic FizzBuzz problem to ensure correct output for multiples of 3, 5, and both.
    

This day was instrumental in developing systematic debugging approaches and improving problem-solving abilities.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_013_Debugging_Exercises
    ```

3. **Run the Python Script:**
    
    ```
    python debugging_exercises.py
    ```


## Debugging Exercises and Solutions

Below are the original buggy codes and their corrected versions, demonstrating the debugging process.

### Exercise 1: Odd or Even

**Original Buggy Code:**

```
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

**Bug(s) Identified:** The **`=`** is an **assignment operator** used to assign values, while the **`==`** is a **comparison operator** used to check if two values are equal. Using `=` would cause a **syntax error** since Python expects an expression to the right of it, not a comparison.

**Corrected Code:**

```
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

### Exercise 2: Leap Year

**Original Buggy Code:**

```
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
```

**Bug(s) Identified:**

1. **Type Error:** The `input()` function returns a string. `year` was not converted to an integer before performing modulo operations, leading to a `TypeError`.
    

**Corrected Code:**

```
year = int(input("Which year do you want to check?")) # Corrected: Convert input to int

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
```

### Exercise 3: FizzBuzz

**Original Buggy Code:**

```
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print(number)
```

**Bug(s) Identified:**

1. **Incorrect Order of Conditions:** The `if number % 3 == 0 or number % 5 == 0:` condition should be `if number % 3 == 0 and number % 5 == 0:` and placed _first_ to correctly handle numbers divisible by both 3 and 5 (e.g., 15).
    
2. **Separate `if` statements:** The `if number % 3 == 0:` and `if number % 5 == 0:` were separate `if` statements instead of `elif`, causing multiple outputs for the same number (e.g., for 15, it would print "FizzBuzz", then "Fizz", then "Buzz").
    
3. **Misplaced `else`:** The `else: print(number)` was incorrectly attached only to the last `if number % 5 == 0:`, meaning numbers not divisible by 5 (but possibly by 3) would still print their number in addition to "Fizz".
    

**Corrected Code:**

```
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # Corrected: Use 'and' and place first
    print("FizzBuzz")
  elif number % 3 == 0: # Corrected: Use 'elif'
    print("Fizz")
  elif number % 5 == 0: # Corrected: Use 'elif'
    print("Buzz")
  else: # Corrected: Correctly placed 'else' for numbers not divisible by 3 or 5
    print(number)
```

## Concepts Reinforced

- **Reading Error Messages:** Understanding `TypeError` and other common runtime errors.
    
- **Logical Flow:** Carefully tracing the execution path of conditional statements.
    
- **Order of Operations:** The importance of condition order in `if/elif/else` blocks.
    
- **Input Data Types:** Always being mindful of the data type returned by `input()`.
    
- **Systematic Debugging:** Using print statements or a debugger to inspect variable values at different stages.
    
## Author

[Musn0o](https://github.com/Musn0o)