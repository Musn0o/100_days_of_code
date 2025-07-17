# Day_064_My_Top_10_Movies_Website

This project is part of my 100 Days of Code journey.

## Project Description

On Day 64, the focus was on building a **My Top 10 Movies Website** using **Flask**, integrating a **database** for persistent storage and full **CRUD (Create, Read, Update, Delete)** functionality. This project consolidated many previously learned web development concepts:

1. **Flask-SQLAlchemy:** Using SQLAlchemy as an Object Relational Mapper (ORM) to interact with a SQLite database, defining a `Movie` model to represent movie data.
    
2. **Database Persistence:** Storing movie data permanently in `top-movies.db`, ensuring data is not lost when the server restarts.
    
3. **Flask-WTF for Forms:** Implementing forms for adding new movies and editing existing movie ratings/reviews, complete with validation.
    
4. **CRUD Operations:**
    
    - **Create:** Adding new movies to the database via a web form.
        
    - **Read:** Displaying all movies from the database on the home page, sorted by rating and dynamically assigned a rank.
        
    - **Update:** Modifying a movie's rating and review through a dedicated edit page.
        
    - **Delete:** Removing movies from the database.
        
5. **Dynamic Rendering:** Using Jinja2 templates to display movie cards, forms, and messages.
    
6. **Flask-Bootstrap:** Applying Bootstrap for responsive and attractive styling.
    
7. **Image Handling:** Displaying movie posters using provided image URLs.
    

The application allows users to curate their personal top 10 (or more) movie list, add new entries, update details, and remove movies, all with persistent storage.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_064_My_Top_10_Movies_Website
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install Flask Flask-Bootstrap5 Flask-SQLAlchemy Flask-WTF
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Home Page (`/`):** Initially, it will show "No movies in your list yet." with an "Add Movie" button. After adding movies, they will appear as styled cards, ranked by rating.
    
- **Add Movie (`/add`):** Presents a form to enter movie details (title, year, description, image URL). Upon submission, the movie is added to the database.
    
- **Edit Movie (`/edit/<id>`):** Clicking "Update" on a movie card takes you to an edit page where you can change its rating and review.
    
- **Delete Movie (`/delete/<id>`):** Clicking "Delete" on a movie card removes it from the database.
    

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Database Integration:** Connecting Flask with SQLite using SQLAlchemy.
    
- **ORM (SQLAlchemy):** Defining database models and performing CRUD operations using Python objects.
    
- **Persistent Data:** Storing and retrieving data that survives server restarts.
    
- **Full CRUD Functionality:** Implementing all four fundamental database operations.
    
- **Dynamic Ranking:** Calculating and displaying ranks based on data attributes.
    
- **Web Forms with Validation:** Robust handling of user input for database operations.
    
- **Modular Web Design:** Structuring a more complex web application.

## Author
[Musn0o](https://github.com/Musn0o)