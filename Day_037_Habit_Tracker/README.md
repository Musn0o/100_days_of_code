# Day_037_Habit_Tracker

This project is part of my 100 Days of Code journey.

## Project Description

On Day 37, the focus was on building a **Habit Tracker** by interacting with the **Pixela API**. This project provided hands-on experience with:

1. **API Interaction (POST, PUT, DELETE):** Making various types of HTTP requests to create, update, and delete data on an external service.
    
2. **API Authentication:** Using tokens and headers for secure API access.
    
3. **JSON Data:** Sending and receiving data in JSON format.
    
4. **Date and Time Manipulation:** Using Python's `datetime` module to work with dates for habit tracking.
    
5. **User-Defined Endpoints:** Understanding how to construct specific URLs for different API operations.
    
6. **Building a Digital Habit Tracker:** Creating a programmatic way to track daily progress on a habit.
    

The application demonstrates how to create a user account on Pixela, define a habit graph, post daily "pixels" (representing completed habit units), update existing pixels, and even delete them. This allows for a visual representation of habit streaks and progress.

## How to Run

This project requires you to create a Pixela account and obtain your user token.

1. **Obtain Pixela Credentials:**
    
    - Sign up at [Pixela](https://pixe.la/ "null") to get your username and a personal token. You'll also define a graph ID for your habit.
        
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_037_Habit_Tracker
    ```
    
    (Ensure this path matches the exact folder name you use for this project in your repository.)
    
4. **Install Required Libraries:**
    
    ```
    pip install requests
    ```
    
5. **Configure Credentials:** Open the `main.py` file and replace the placeholder values for `PIXELA_USERNAME`, `PIXELA_TOKEN`, and `GRAPH_ID` with your actual Pixela credentials.
    
6. **Run the Python Script:**
    
    ```
    python main.py
    ```
    
    _(Note: The script will execute the API calls sequentially. You might want to comment out sections (e.g., user creation, graph creation, deletion) after their initial successful run to avoid errors on subsequent runs.)_
    

## Demo

When you run the script, it will perform a series of API calls. The console output will show the responses from the Pixela API, indicating success or failure of each operation (user creation, graph creation, pixel posting, updating, deleting). You can then visit your Pixela graph URL (e.g., `https://pixe.la/v1/users/YOUR_USERNAME/graphs/YOUR_GRAPH_ID.html`) in a web browser to see the visual representation of your habit tracking.

```
# Example console output (actual output depends on Pixela API response):
{"message":"User created successfully","isSuccess":true}
{"message":"Graph created successfully","isSuccess":true}
{"message":"Successfully created.","isSuccess":true}
{"message":"Successfully updated.","isSuccess":true}
{"message":"Successfully deleted.","isSuccess":true}
```

## Concepts Learned

- **RESTful APIs:** Understanding the principles of REST (Representational State Transfer) and how to interact with RESTful services.
    
- **HTTP Methods:** Practical use of `POST` (create), `PUT` (update), and `DELETE` (delete) requests.
    
- **Request Headers:** Sending authentication tokens and other metadata in HTTP headers.
    
- **JSON Payloads:** Constructing and sending data in JSON format for API requests.
    
- **Error Handling (API):** Interpreting API responses to determine success or failure.
    
- **Automated Data Submission:** Programmatically updating data on a web service.

## Author

[Musn0o](https://github.com/Musn0o)