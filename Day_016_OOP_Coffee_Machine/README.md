# # Day_016_OOP_Coffee_Machine

This project is part of my 100 Days of Code journey.

## Project Description

On Day 16, the focus shifted dramatically to **Object-Oriented Programming (OOP)** by re-building the Coffee Machine from Day 15 using OOP principles. This project was a crucial introduction to:

- **Classes and Objects:** Understanding how to define custom classes (`Menu`, `MenuItem`, `CoffeeMaker`, `MoneyMachine`) and create objects (instances) from them.
    
- **Attributes:** Storing data within objects (e.g., `resources` in `CoffeeMaker`, `cost` in `MenuItem`).
    
- **Methods:** Defining functions that belong to objects and operate on their attributes (e.g., `make_coffee()` in `CoffeeMaker`, `is_sufficient()` in `CoffeeMaker`, `process_coins()` in `MoneyMachine`).
    
- **Encapsulation:** Bundling data (attributes) and methods that operate on the data within a single unit (the class).
    
- **Modularity:** Organizing code into separate, reusable classes, making the program more maintainable and scalable compared to the procedural approach.
    
- **External Libraries:** (Implicitly, if using pre-built classes like `PrettyTable` or `Turtle` in other contexts, though not strictly for this core project).
    

The simulation still mimics a real-world coffee machine, but its internal logic is now structured using objects, demonstrating the power and benefits of OOP for managing complexity.

## How to Run

This project typically involves multiple Python files (e.g., `main.py`, `menu.py`, `coffee_maker.py`, `money_machine.py`). Ensure all files are in the same directory.

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_016_OOP_Coffee_Machine
    ```

3. **Run the Main Python Script:**
    
    ```
    python main.py
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

- **OOP Fundamentals:** Core concepts of classes, objects, attributes, and methods.
    
- **Code Organization:** How OOP helps in structuring larger programs.
    
- **Reusability:** Designing classes that can be reused in different parts of an application or other projects.
    
- **Abstraction:** Interacting with objects through their methods without needing to know their internal implementation details.
    
- **Problem Decomposition with OOP:** Breaking down a problem into distinct entities (objects) that interact with each other.
    

## Author

[Musn0o](https://github.com/Musn0o)