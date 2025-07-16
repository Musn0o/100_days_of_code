# Welcome message for the tip calculator
print("Welcome to the tip calculator!")

# Get the total bill amount from the user
# Convert the input string to a float to handle decimal values.
total_bill = float(input("What was the total bill? $\n"))

# Get the desired tip percentage from the user
# Convert the input string to an integer.
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

# Get the number of people to split the bill
# Convert the input string to an integer.
num_people = int(input("How many people to split the bill?\n"))

# Calculate the tip amount
# Convert tip_percentage to a decimal (e.g., 12 becomes 0.12)
tip_as_decimal = tip_percentage / 100
tip_amount = total_bill * tip_as_decimal

# Calculate the total bill including the tip
bill_with_tip = total_bill + tip_amount

# Calculate the amount each person should pay
# Divide the total bill with tip by the number of people.
amount_per_person = bill_with_tip / num_people

# Format the final amount to two decimal places, suitable for currency
# The round() function can be tricky with floating point, so f-string formatting is often preferred for display.
final_amount = "{:.2f}".format(amount_per_person)

# Print the result to the user
print(f"Each person should pay: ${final_amount}")

