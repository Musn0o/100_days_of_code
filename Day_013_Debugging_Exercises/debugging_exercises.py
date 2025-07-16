# --- Day 13: Debugging Exercises ---

# This file contains the original buggy code for the Day 13 debugging exercises,
# followed by the corrected versions. This allows you to compare and understand
# the common pitfalls and how to fix them.

# --- Exercise 1: Odd or Even ---
print("\n--- Exercise 1: Odd or Even ---")

# Original Buggy Code (No actual bug in the course's version, this was a warm-up)
# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

# Corrected Code (Same as original, as it was already correct)
print("Original code (which was already correct):")
number_oe = int(input("Which number do you want to check? "))

if number_oe % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

print("--- End of Exercise 1 ---")

# --- Exercise 2: Leap Year ---
print("\n--- Exercise 2: Leap Year ---")

# Original Buggy Code
# year = input("Which year do you want to check? ")
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# Bug: The 'year' input was a string and needed to be converted to an integer
# before performing modulo operations. This would cause a TypeError.

# Corrected Code
print("Corrected code:")
year_ly = int(input("Which year do you want to check? ")) # Bug fix: Convert input to int

if year_ly % 4 == 0:
  if year_ly % 100 == 0:
    if year_ly % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

print("--- End of Exercise 2 ---")

# --- Exercise 3: FizzBuzz ---
print("\n--- Exercise 3: FizzBuzz ---")

# Original Buggy Code
# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0: # This should be 'and' and come first
#     print("FizzBuzz")
#   if number % 3 == 0: # This should be 'elif'
#     print("Fizz")
#   if number % 5 == 0: # This should be 'elif'
#     print("Buzz")
#   else: # This 'else' is incorrectly attached only to the last 'if'
#     print(number)

# Bugs:
# 1. Incorrect order of conditions: `if number % 3 == 0 or number % 5 == 0:`
#    should be `if number % 3 == 0 and number % 5 == 0:` and placed first.
# 2. Separate `if` statements instead of `elif`: This caused multiple outputs
#    for numbers divisible by both 3 and 5 (e.g., 15 would print "FizzBuzz", "Fizz", "Buzz").
# 3. Misplaced `else`: The `else: print(number)` was only linked to the last `if`.

# Corrected Code
print("Corrected code:")
for number_fb in range(1, 101):
  if number_fb % 3 == 0 and number_fb % 5 == 0: # Bug fix: Use 'and' and place first
    print("FizzBuzz")
  elif number_fb % 3 == 0: # Bug fix: Use 'elif'
    print("Fizz")
  elif number_fb % 5 == 0: # Bug fix: Use 'elif'
    print("Buzz")
  else: # Bug fix: Correctly placed 'else' for numbers not divisible by 3 or 5
    print(number_fb)

print("--- End of Exercise 3 ---")

