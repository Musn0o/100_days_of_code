# Day_059_Blog_Capstone_Project_Part2

This project is part of my 100 Days of Code journey.

## Project Description

On Day 59, I continued developing the **Blog Capstone Project**, focusing on creating a more structured and visually appealing web application using **Flask** and **Jinja2 templating**. This part built upon Day 57's foundation by introducing:

1. **Template Inheritance (`extends`):** Implementing a base template (`base.html` or similar, though here we'll use `header.html` and `footer.html` includes for simplicity as often taught in this context) to define common elements (like header and footer) that are reused across multiple pages.
    
2. **Template Includes (`include`):** Using `{% include 'header.html' %}` and `{% include 'footer.html' %}` to insert reusable sections of HTML into different templates.
    
3. **Serving Static Files:** Properly linking and serving static assets like CSS stylesheets from a dedicated `static` folder to control the look and feel of the blog.
    
4. **Improved Styling:** Applying basic CSS to create a cleaner and more readable blog layout.
    
5. **Local Data Source:** Using a local list of dictionaries to simulate blog post data, making the project self-contained without external API dependencies.
    

This project demonstrates how to build a well-structured Flask application using templating best practices for a consistent and maintainable web presence.

## How to Run

This project requires a specific folder structure:

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_059_Blog_Capstone_Project_Part2
    ```
    
3. **Install Required Libraries:**
    
    ```
    pip install Flask
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Home Page (`/`):** You will see a blog home page with a header, a list of blog post titles and short excerpts, and a footer. Each post title will be a link.
    
- **Individual Post Page (`/post/<post_id>`):** Clicking on a post title will take you to a new page displaying the full title and body of that specific blog post, also with the consistent header and footer.
    

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Jinja2 Template Organization:** Effective use of `include` for modularity.
    
- **Static File Management:** Proper linking of CSS for styling.
    
- **Consistent UI:** Maintaining a uniform look and feel across different pages using shared template components.
    
- **Local Data Handling:** Managing application data directly within the Python script (or a separate data file).
    
- **Backend-Frontend Integration:** How Flask dynamically serves structured data to styled HTML pages.

## Author

[Musn0o](https://github.com/Musn0o)