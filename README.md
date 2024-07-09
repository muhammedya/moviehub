# Django Movie Review App

## Project Description:

This is a web application built using Django, designed to manage movie reviews. The app allows users to create, read, update, and delete movie details. Each movie entry includes the movie title, release date, description, and a poster photo. This project is a great starting point for beginners to learn Django's functionality and features.

## Features

- **Movie Creation:** Add new movies to the database with relevant details.
- **Movie Editing:** Update existing movie details.
- **Movie Deletion:** Remove movies from the database.
- **Movie Details View:** View individual movie details including the title, release date, description, and poster.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/muhammedya/moviehub/tree/master
   cd moviepro
   ```

2.1 **Create a virtual environment and activate it:(on Linux or Mac)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2.2 **Create a virtual environment and activate it:(on Windows)**
   ```bash
   virtualenv venv
   venv/Scripts/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py createsuperuser
   ```
   
5. **Run the Development Server:**
   Open your web browser and go to http://127.0.0.1:8000.


## Future Enhancements: (work in progress)

- **User Authentication:** Allow users to register, log in, and manage their own movie reviews.
- **Movie Reviews:** Add functionality for users to leave reviews and ratings for each movie.
- **Search Functionality:** Add functionality for users to leave reviews and ratings for each movie.
- **Pagination:** Add functionality for users to leave reviews and ratings for each movie.
- **Responsive Design:** Add functionality for users to leave reviews and ratings for each movie.
