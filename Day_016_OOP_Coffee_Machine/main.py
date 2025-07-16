# --- main.py ---
# This is the main script to run the OOP Coffee Machine.
# It imports and uses the classes defined in other files.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create instances (objects) of our machine components
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Flag to keep the coffee machine running
is_on = True

# Main loop for the coffee machine operation
while is_on:
    # Get available drink options from the menu
    options = menu.get_items()
    # Prompt the user for their choice
    choice = input(f"What would you like? ({options}): ").lower()

    # Check for special commands
    if choice == "off":
        is_on = False # Turn off the machine
    elif choice == "report":
        # Print reports from both the coffee maker and money machine
        coffee_maker.report()
        money_machine.report()
    else:
        # Get the MenuItem object corresponding to the user's choice
        drink = menu.find_drink(choice)
        # Check if the drink exists and if resources are sufficient
        if drink: # Ensure drink is not None (i.e., found a valid drink)
            if coffee_maker.is_resource_sufficient(drink):
                # Process payment if resources are sufficient
                if money_machine.make_payment(drink.cost):
                    # Make the coffee if payment is successful
                    coffee_maker.make_coffee(drink)