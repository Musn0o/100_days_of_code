# Day_045_100_Movies_To_Watch

This project is part of my 100 Days of Code journey.

## Project Description

On Day 45, the focus was on **Web Scraping** using Python to compile a list of "100 Movies To Watch." This project specifically involved:

1. **HTTP Requests with `requests`:** Fetching the HTML content of a target webpage (e.g., a "100 Greatest Films" list).
    
2. **HTML Parsing with Beautiful Soup:** Using Beautiful Soup to navigate and parse the raw HTML data.
    
3. **Targeted Data Extraction:** Identifying and extracting specific elements, primarily the movie titles, from the webpage's structure.
    
4. **Data Storage:** Saving the extracted movie titles into a local text file (`movies.txt`), with each movie on a new line.
    
5. **List Manipulation:** Reversing the order of the movies if the source list is in descending order (e.g., 100 to 1) to get them in ascending order (1 to 100).
    

The application automates the process of creating a personalized movie watchlist by scraping a popular movie list from the internet.

## How to Run

1. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
2. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_045_100_Movies_To_Watch
    ```

3. **Install Required Libraries:**
    
    ```
    pip install requests beautifulsoup4
    ```
    
4. **Run the Python Script:**
    
    ```
    python main.py
    ```

## Demo

When you run the script, it will fetch the content from the specified URL, extract the movie titles, and save them into a file named `movies.txt` in the same directory. The console output will typically show a confirmation or the list of movies as they are extracted.

**Example `movies.txt` content:**

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
5) Pulp Fiction
6) Goodfellas
7) Raiders Of The Lost Ark
8) Jaws
9) Star Wars
10) The Lord Of The Rings: The Fellowship Of The Ring
... (up to 100 movies)
```

## Concepts Learned

- **Web Scraping Workflow:** The complete process from fetching HTML to parsing and saving data.
    
- **Beautiful Soup Advanced Usage:** More complex selection methods to pinpoint specific data within a webpage.
    
- **File I/O:** Reading from and writing to text files in Python.
    
- **Data Structuring:** Organizing scraped data into a usable format (e.g., a list of strings).
    
- **Handling Web Content:** Understanding how to deal with the dynamic and often inconsistent nature of web pages.

## Author

[Musn0o](https://github.com/Musn0o)