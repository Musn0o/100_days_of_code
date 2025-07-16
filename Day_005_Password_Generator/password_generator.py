import random
import string

print("Welcome to the PyPassword Generator!")

# Get user input for desired character types
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


# # Define lists of possible characters for the password
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Define character sets
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

password_list = []

# Add random letters to the password list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle the entire password list to randomize character order
random.shuffle(password_list)

# Join the list of characters into a single string
password = "".join(password_list)

print(f"Your generated password is: {password}")
