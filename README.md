<h1>To-Do List Web Application</h1>
This is a web application that provides a to-do list functionality, allowing users to create, read, update, and delete tasks. It also includes user registration, login, and search functionality. The application is built using Django, a Python web framework.

Getting Started
To run this application locally, follow these steps:

Clone this repository: git clone https://github.com/katurivinay/todo-app-using-class-based-views.git

Navigate to the project directory: cd todo-app-using-class-based-views

Install the required dependencies: pip install -r requirements.txt

Set up the database: python manage.py migrate

Create a superuser account: python manage.py createsuperuser

Start the development server: python manage.py runserver

Access the application in a web browser at http://localhost:8000/

Usage
User Registration and Login
To use the application, users must first register for an account by clicking on the "Register" link in the top navigation bar. Once registered, users can log in to their account by clicking on the "Log In" link in the top navigation bar and entering their credentials.

Creating Tasks
Once logged in, users can create new tasks by clicking on the "New Task" button in the top navigation bar. They will be taken to a form where they can enter the details of the task, including its title and description.

Viewing Tasks
To view a list of all tasks, click on the "Tasks" link in the top navigation bar. This will display a list of all tasks that have been created by the user. Users can click on individual tasks to view their details.

Updating Tasks
To update a task, users can click on the "Edit" button next to the task they wish to update. They will be taken to a form where they can edit the details of the task.

Deleting Tasks
To delete a task, users can click on the "Delete" button next to the task they wish to delete. They will be prompted to confirm their action before the task is permanently deleted.

Searching Tasks
Users can search for specific tasks using the search bar in the top navigation bar. They can enter a search term and click the "Search" button to find all tasks that match the search criteria.

