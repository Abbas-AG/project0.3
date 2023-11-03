# Commercial Offer and Reservation Management System
## Introduction
Welcome to the Commercial Offer and Reservation Management System! This is a web application that I created for the final project of web50x. This application allows customers to view and book company services, such as room reservations and coffee breaks, in a convenient and user-friendly way. It also provides contact information for the company and a feedback form for the customers.

## Distinctiveness and Complexity
This project satisfies the distinctiveness and complexity requirements of the course for the following reasons:

1-It is not based on any of the previous projects in the course, nor on the old CS50W Pizza project. It is a unique idea that I came up with, inspired by my own experience as a customer of various companies.

2-It is not a social network or an e-commerce site. It is a service-oriented application that focuses on providing customers with a smooth and satisfying booking experience. It also allows the company to manage their offers and reservations in an efficient and secure way.

3-It utilizes Django on the back-end and JavaScript on the front-end, as well as HTML and CSS for the layout and design.

4-It is mobile-responsive, meaning that it adapts to different screen sizes and devices. It uses media queries to achieve this.

5-It is more complex than the previous projects in the course, as it involves multiple models, views, templates, forms, and APIs. It also implements validation, error handling, and data visualization features.

## File Structure

### The project consists of the following files and directories: 

manage.py: The main script that runs the Django server and executes various commands.

requirements.txt: The file that lists the Python packages that need to be installed to run the application.

commercial: The main Django app that contains the settings, urls, and wsgi files for the project.

static: The directory that contains the static files, such as images, CSS, and JavaScript files.

media: The directory that contains the uploaded files, such as user profile pictures and company logos.

## How to Run

### To run the application, follow these steps:

1-Clone the repository to your local machine.

2-Create and activate a virtual environment.

3-Install the Python packages from the requirements.txt file.

4-Make migrations and migrate the database.

5-Create a superuser account.

6-Run the Django server.

7-Access the application from your browser.

## Additional Information

### Here are some additional information that the staff should know about the project:

The application uses SQLite as the database engine, which is the default for Django. However, it can be easily changed to another engine, such as PostgreSQL, by modifying the DATABASES setting in the commercial/settings.py file.

The application uses the Django admin interface to manage the models and data. The superuser account can access this interface from the /admin URL.

