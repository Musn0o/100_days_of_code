# Day_062_Coffee_And_WiFi_Project

This project is part of my 100 Days of Code journey.

## Project Description

On Day 62, the focus was on building a **Coffee & WiFi Directory Web Application** using **Flask**, integrating advanced form handling and basic data persistence. This project combined several key web development concepts:

1. **Flask-WTF for Forms:** Implementing robust web forms using Flask-WTF for creation, validation, and rendering. This includes various field types (`StringField`, `SelectField`) and validators (`DataRequired`, `URL`).
    
2. **Flask-Bootstrap for Styling:** Integrating Flask-Bootstrap to quickly add responsive and attractive styling to the web application without writing extensive custom CSS.
    
3. **CSV Data Persistence:** Storing the coffee shop data in a simple CSV file (`cafe-data.csv`), demonstrating basic file I/O for data storage and retrieval.
    
4. **Handling Form Submissions:** Processing `POST` requests from the form, validating data, and appending new cafe entries to the CSV file.
    
5. **Displaying Tabular Data:** Reading data from the CSV and rendering it dynamically in an HTML table on a dedicated `/cafes` route.
    
6. **Dropdowns and Choices:** Using `SelectField` to provide predefined options for WiFi strength, power availability, and seating capacity.
    

The application allows users to add new coffee shops to a directory, providing details like name, location, opening/closing times, and crucial amenities for remote workers (WiFi, power, seating). All entries are then viewable in a structured table.

## How to Run

1. **Create `cafe-data.csv`:** In the root of your project directory, create an empty file named `cafe-data.csv`. The script will add headers if it's truly empty.
    
2. **Clone the Repository:**
    
    ```
    git clone https://github.com/Musn0o/100_days_of_code.git
    ```
    
3. **Navigate to the Project Directory:**
    
    ```
    cd 100_days_of_code/Day_062_Coffee_And_WiFi_Project
    ```
    
4. **Install Required Libraries:**
    
    ```
    pip install Flask Flask-WTF Flask-Bootstrap
    ```
    
5. **Run the Python Script:**
    
    ```
    python main.py
    ```
    

## Demo

After running the `main.py` script, open your web browser and navigate to `http://127.0.0.1:5000/`.

- **Home Page (`/`):** Displays a welcome message and links to "Add New Cafe" and "View All Cafes."
    
- **Add New Cafe (`/add`):** Presents a form to enter details about a coffee shop. Fill out the form and submit it. Upon successful submission, the data will be saved to `cafe-data.csv`.
    
- **View All Cafes (`/cafes`):** Displays all the coffee shops currently stored in `cafe-data.csv` in a nicely formatted table.
    

_(Note: The output is displayed in a web browser, not the console.)_

## Concepts Learned

- **Flask-WTF:** Advanced form creation, validation, and rendering.
    
- **Flask-Bootstrap:** Rapid prototyping and styling with a popular CSS framework.
    
- **CSV File I/O:** Reading from and writing to CSV files for simple data storage.
    
- **Data Validation:** Ensuring data integrity before saving.
    
- **Web Forms:** Building interactive forms for user input.
    
- **Templating with Macros:** Using Jinja2 macros (e.g., `wtf.quick_form`) for concise form rendering.
    
- **HTTP Methods (`GET`, `POST`):** Handling different request types for form submission.

## Author
[Musn0o](https://github.com/Musn0o)