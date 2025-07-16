# Day 6: Escaping the Maze with Reeborg's World

This project focuses on **Python functions, code blocks, `while` loops, and conditional statements (`if`/`elif`/`else`)** by solving a maze challenge using **Reeborg's World**.

## 🎯 Project Goal

The objective was to program Reeborg, a virtual robot, to navigate and escape a complex maze. The solution implemented a strategy where Reeborg would prioritize turning right (following the right-hand wall), moving forward if the front is clear, and turning left as a last resort when blocked.

## 🤖 How to Run (External Environment)

This code is designed to be executed within the Reeborg's World online environment.

1.  Go to [Reeborg's World](https://reeborg.ca/).
2.  Select the "Maze" world (or the specific Hurdle challenge you completed).
3.  Paste the code from `main.py` into the Python code editor on the Reeborg's World website.
4.  Click the "Run" (play) button to see Reeborg solve the maze.

## 💡 Key Concepts Learned

* **Functions:** Defining and calling reusable blocks of code (e.g., `turn_right()`).
* **`while` loops:** Repeating actions until a certain condition is met (e.g., `while not at_goal():`).
* **Conditional Logic (`if`/`elif`/`else`):** Making decisions based on the robot's surroundings (e.g., `wall_on_right()`, `front_is_clear()`, `at_goal()`).
* **Code Blocks and Indentation:** Understanding the importance of indentation in Python for defining code blocks.

## My Solution Strategy

The core logic of the maze-solving algorithm follows the "right-hand rule":
1. If the robot can turn right, it does so and moves forward.
2. Else if the robot can move forward, it does so.
3. Else (if blocked in front and unable to turn right), it turns left.
This strategy ensures the robot will eventually find the exit in any simple maze where an exit exists.

---

[Musn0o](https://github.com/Musn0o)