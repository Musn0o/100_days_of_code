# Day_057_Blog_Capstone_Project_Part1

  

This project is part of my 100 Days of Code journey.

  

## Project Description

  

On Day 57, I began building a **Blog Capstone Project** using the **Flask** web framework. This first part focused on integrating with an external API to fetch blog post data and dynamically rendering it using HTML templates. Key concepts covered include:

  

1. **External API Integration (`requests`):** Making HTTP GET requests to a public API (e.g., JSONPlaceholder) to retrieve a list of blog posts.

2. **Dynamic Data Rendering (Jinja2 Templating):**

- Passing Python data (list of blog posts) from the Flask application to HTML templates.

- Using Jinja2 syntax (`{% for %}`, `{{ }}`) within `index.html` to loop through the data and display each blog post.

- Creating a separate `post.html` template to display individual blog posts dynamically based on their ID.

3. **Flask Routing with Dynamic Paths:** Defining routes that accept variable parts (e.g., `/<int:post_id>`) to serve individual blog post pages.

4. **Modular Web Application:** Structuring the Flask application to fetch data and render different pages based on user requests.

  

This project lays the foundation for a full-fledged blog, demonstrating how to populate web pages with content from external sources.

  

## How to Run
  

1. **Clone the Repository:**

```

git clone https://github.com/Musn0o/100_days_of_code.git

```

2. **Navigate to the Project Directory:**

```

cd 100_days_of_code/Day_057_Blog_Capstone_Project_Part1

```



3. **Install Required Libraries:**

```

pip install Flask requests

```

4. **Run the Python Script:**

```

python main.py

```

  

## Demo

  

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

  

- **Home Page (`/`):** You will see a list of blog post titles, each acting as a link.

- **Individual Post Page (`/post/<post_id>`):** Clicking on a post title will take you to a new page displaying the full title and body of that specific blog post.

  

_(Note: The output is displayed in a web browser, not the console.)_

  

## Concepts Learned

  

- **API Consumption:** Fetching and using data from external web services.

- **Dynamic Web Pages:** Generating HTML content based on data.

- **Jinja2 Templating:** Using template inheritance and control structures (`for` loops) in HTML.

- **URL Parameters:** Passing data through URLs to retrieve specific content.

- **Backend-Frontend Interaction:** How a Flask backend provides data to a frontend HTML template.

  

## Author

  

[Musn0o](https://github.com/Musn0o)