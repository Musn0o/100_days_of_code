# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")

# 2. Ask the user for the city that they grew up in.
# The input() function prompts the user and returns their input as a string.
city = input("What's the name of the city you grew up in?\n")

# 3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")

# 4. Combine the name of their city and pet to show them their band name.
# String concatenation (+) is used to join the two strings together.
# A space is added between the city and pet name for readability.
band_name = city + " " + pet

# 5. Display the generated band name.
# An f-string is used for clear and concise output formatting.
print(f"Your band name could be {band_name}")

