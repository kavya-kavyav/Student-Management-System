# Student-Management-System
# Student Management System

A simple web-based Student Management System built with **Python,
FastAPI, HTML, CSS, and SQLite**. This project demonstrates the basic
concepts of FastAPI and how a frontend can communicate with a backend to
manage student records.

## Features

The application supports all four CRUD operations:

-   **Create:** Add a new student record.
-   **Read:** View the list of students and their details.
-   **Update:** Edit an existing student's information.
-   **Delete:** Remove a student record.

Student information can include:

-   Student ID
-   Name
-   Age
-   Gender
-   Marks
-   Course
-   Image
-   Status

## Technologies Used

  Technology         Purpose
  ------------------ -----------------------------------------------
  Python             Backend programming
  FastAPI            Building backend routes and handling requests
  SQLite             Storing student records
  HTML               Creating the web page structure
  CSS                Styling the user interface
  Jinja2 Templates   Rendering dynamic HTML pages
  Pydantic           Validating and managing data models

## Project Structure

A possible project structure is shown below. Adjust the filenames to
match your actual project.

``` text
Student-Management-System/
│
├── main.py                 # FastAPI application and routes
├── students.db             # SQLite database (created by the app)
├── templates/              # HTML templates
│   ├── home.html
│   ├── add_student.html
│   └── update_student.html
│
├── static/                 # CSS, images, and other static files
│   └── style.css
│
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation and Setup

### 1. Clone the repository

``` bash
git clone <your-github-repository-url>
```

### 2. Open the project folder

``` bash
cd Student-Management-System
```

### 3. Create a virtual environment (recommended)

``` bash
python -m venv venv
```

Activate it on Windows:

``` bash
venv\Scripts\activate
```

### 4. Install dependencies

If you have a `requirements.txt` file:

``` bash
pip install -r requirements.txt
```

Otherwise, install the main packages:

``` bash
pip install fastapi uvicorn jinja2 python-multipart
```

### 5. Run the application

If your FastAPI application instance is named `app` inside `main.py`,
run:

``` bash
uvicorn main:app --reload
```

If your Python file has a different name, replace `main` with that
filename (without `.py`).

### 6. Open the application

Visit the local address shown in your terminal. FastAPI's interactive
API documentation is normally available at:

``` text
http://127.0.0.1:8000/docs
```

## How It Works

1.  The user interacts with the HTML pages in the browser.
2.  FastAPI receives the request through the corresponding route.
3.  The backend validates and processes the submitted data.
4.  SQLite stores, retrieves, updates, or deletes student records.
5.  The application returns the updated page or response to the user.

## Concepts Practiced

-   FastAPI application setup and route creation
-   HTTP methods and CRUD operations
-   Handling HTML form data
-   Request and response handling
-   Pydantic models and data validation
-   SQLite database connectivity and SQL queries
-   Dynamic HTML rendering with Jinja2 templates
-   Connecting frontend pages with backend routes

## Learning Outcomes

Building this project provided practical experience with FastAPI
fundamentals and helped me understand how frontend pages, backend
routes, data validation, and database operations work together in a web
application.

## Future Enhancements

-   Add user authentication and login.
-   Add search and filter options for student records.
-   Improve form validation and error handling.
-   Add pagination for student lists.
-   Improve the user interface and responsiveness.

## Author

**Your Name**

## Acknowledgements

Special thanks to **Mentor Sai Balaji** for the guidance and support
throughout this learning journey.

Thanks to **Innomatics Research Labs** and **Full Stack Experts
Academy** for providing the opportunity to learn and build this project.

------------------------------------------------------------------------

If you find this project useful, feel free to explore the code and learn
from it.
