# ASCII art for the calculator logo
logo = """
  _ __ __ _ _ __   __ _  ___ _ __
 | '__/ _` | '_ \\ / _` |/ _ \\ '__|
 | | | (_| | | | | (_| |  __/ |
 |_|  \__,_|_| |_|\__, |\___|_|
                  |___/
"""

# Function for addition
def add(n1, n2):
  return n1 + n2

# Function for subtraction
def subtract(n1, n2):
  return n1 - n2

# Function for multiplication
def multiply(n1, n2):
  return n1 * n2

# Function for division
def divide(n1, n2):
  # Basic error handling for division by zero
  if n2 == 0:
    return "Error: Cannot divide by zero!"
  return n1 / n2

# Dictionary mapping operation symbols to their corresponding functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Main calculator function
def calculator():
  print(logo) # Display the calculator logo

  # Get the first number from the user
  num1 = float(input("What's the first number?: "))

  # Display available operation symbols
  for symbol in operations:
    print(symbol)

  should_continue = True # Flag to control the calculation loop

  while should_continue:
    # Get the operation symbol from the user
    operation_symbol = input("Pick an operation: ")

    # Get the next number from the user
    num2 = float(input("What's the next number?: "))

    # Get the function associated with the chosen operation symbol from the dictionary
    calculation_function = operations[operation_symbol]

    # Perform the calculation
    answer = calculation_function(num1, num2)

    # Print the result of the current operation
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Check if the user wants to continue calculating with the current answer,
    # start a new calculation, or exit.
    choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation, or 'x' to exit: ").lower()

    if choice == 'y':
      # If 'y', the current answer becomes the first number for the next calculation
      num1 = answer
    elif choice == 'n':
      # If 'n', exit the current loop and call calculator() again to start fresh
      should_continue = False
      calculator() # Recursive call to start a new calculation
    else: # If 'x' or any other input, exit the program
      should_continue = False
      print("Goodbye!")

# Start the calculator program
calculator()
