# --- menu.py ---
# Defines the Menu and MenuItem classes for managing drinks.

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        # Define available menu items
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

    def get_items(self):
        """Returns all the names of the available menu items concatenated as a string."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip('/') # Remove trailing slash

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None
