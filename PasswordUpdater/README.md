# The Star Gazer
A Flask web application to run from a web browser, resulting
in a website that lets you navigate between different html template files 
including user registration, login, and password update pages.

(Under construction) Once an account is created or a current user is logged in, the site redirects to
a page displaying the NASA Picture of the Day. The backend connects to NASA's API to access
the current day's picture.

Backend logic also enforces and validates password complexity and checks for
commonly used passwords. This application also logs failed login attempts to .csv file.

To run the code, you need to set an environmental variable aligned with the file we just created
with the Flask app, and then run flask. In your command prompt, cd to the folder where this file
is located, then run the following commands:

set FLASK_APP=password_update.py

flask run
