from dictionaries import MENU, resources

# Initial profit of the coffee machine
profit = 0

# Function to check if there are sufficient resources to make the chosen drink
def is_resource_sufficient(order_ingredients):
    """Checks if resources are sufficient for the order. Returns True if yes, False if no."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function to process coins inserted by the user
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Function to check if the transaction is successful (enough money, return change)
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit # Access the global profit variable
        profit += drink_cost # Add the cost of the drink to profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# Function to make the coffee and deduct resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

# Main loop to keep the coffee machine running
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

    if choice == "off":
        is_on = False # Turn off the machine
    elif choice == "report":
        # Print current resources and profit
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # Check if the chosen drink is in the menu
        if choice in MENU:
            drink = MENU[choice]
            # Check if resources are sufficient
            if is_resource_sufficient(drink["ingredients"]):
                # Process coins
                payment = process_coins()
                # Check if transaction is successful
                if is_transaction_successful(payment, drink["cost"]):
                    # Make coffee and deduct resources
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice. Please choose from 'espresso', 'latte', 'cappuccino', 'report', or 'off'.")

