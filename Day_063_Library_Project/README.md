# Day_063_Library_Project

This project is part of my 100 Days of Code journey.

## Project Description

On Day 63, the focus was on building a simple **Personal Library Web Application** using **Flask**. This project introduced fundamental concepts of web application development combined with basic data persistence:

1. **Flask-WTF for Forms:** Implementing robust web forms using Flask-WTF for adding new book entries, including validation.
    
2. **In-Memory Data Storage:** Storing the book data in a global Python list of dictionaries. This demonstrates a basic form of data persistence for the duration the application is running (data is lost when the server restarts).
    
3. **CRUD Operations (Create & Read):**
    
    - **Create:** Adding new books to the library via a web form.
        
    - **Read:** Displaying all existing books in a tabular format on the home page.
        
4. **Dynamic Content Rendering:** Using Jinja2 templating to display the list of books and the book submission form.
    
5. **Basic Styling:** Applying minimal CSS to make the interface presentable.
    

The application allows users to add new books (with title, author, and rating) to a collection and view all the books currently in their library.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_063_Library_Project
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install Flask Flask-WTF
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Home Page (`/`):** Initially, it will show "Library is empty." with a link to "Add New Book." After adding books, it will display them in a list.
    
- **Add New Book (`/add`):** Presents a form to enter the book's title, author, and rating. Fill out the form and submit it. Upon successful submission, the book will be added to the in-memory list, and you will be redirected to the home page.
    

_(Note: The output is displayed in a web browser, not the console. Data added will be lost if the Flask server is restarted.)_

## Concepts Learned

- **In-Memory Data Persistence:** Understanding the simplest form of data storage in a running application.
    
- **Flask-WTF:** Practical application of forms with validation.
    
- **CRUD (Create & Read):** Implementing basic operations for managing data.
    
- **Dynamic Table/List Rendering:** Using Jinja2 to display collections of data.
    
- **Web Application Flow:** Navigating between different pages (`/` and `/add`) for different functionalities.

## Author
[Musn0o](https://github.com/Musn0o)