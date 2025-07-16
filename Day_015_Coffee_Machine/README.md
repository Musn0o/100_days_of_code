# Day_015_Coffee_Machine

This project is part of my 100 Days of Code journey.

## Project Description

On Day 15, the focus was on building a **Coffee Machine** simulation. This project was a significant step towards more complex, state-based applications, allowing me to apply and reinforce:

- **Dictionaries:** Storing the `MENU` of coffee types (ingredients, cost) and `resources` available in the machine.
    
- **Functions:** Breaking down the machine's operations into modular functions (e.g., `is_resource_sufficient`, `process_coins`, `is_transaction_successful`, `make_coffee`).
    
- **Loops:** Implementing a `while` loop to keep the coffee machine running, allowing multiple orders.
    
- **Conditional Statements:** Extensive logic for checking resources, processing payments, handling insufficient funds, and making the coffee.
    
- **User Input:** Taking orders and coin inputs from the user.
    
- **Managing State:** Updating the machine's resources and tracking profit.
    

The simulation mimics a real-world coffee machine, handling orders, checking for sufficient ingredients, processing payments, and dispensing the chosen drink while managing internal resources and profit.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_015_Coffee_Machine
    ```

3. **Run the Python Script:**
    
    ```
    python coffee_machine.py
    ```


## Demo

```
What would you like? (espresso/latte/cappuccino/report/off): report
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0.0
What would you like? (espresso/latte/cappuccino/report/off): espresso
Please insert coins.
How many quarters?: 4
How many dimes?: 2
How many nickles?: 0
How many pennies?: 0
Here is $0.25 in change.
Here is your espresso ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino/report/off): report
Water: 250ml
Milk: 200ml
Coffee: 82g
Money: $1.5
What would you like? (espresso/latte/cappuccino/report/off): off
```

## Concepts Learned

- **Object-Oriented Thinking (Basic):** Simulating a real-world object with its own state (resources, profit) and behaviors (making coffee, processing payment).
    
- **State Management:** Tracking and updating the internal state of the machine.
    
- **Input Validation (Implicit):** Handling various user inputs and directing program flow accordingly.
    
- **Financial Calculations:** Performing accurate calculations for payment and change.
    
- **Resource Management:** Checking and deducting resources based on consumption.
    
## Author

[Musn0o](https://github.com/Musn0o)