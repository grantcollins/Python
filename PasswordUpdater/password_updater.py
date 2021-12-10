"""
Flask web application to run from a web browser, resulting
in a website that lets you navigate between different html files
and external links, including user registration, login, and password
update pages.

Enforces password complexity for passwords and checks passwords for
commonly used passwords. Also logs failed login attempts in .csv file.

To run the code, you need to set an environmental variable aligned with the file we just created
with the Flask app, and then run flask. In command prompt, navigate to the folder where this file
is located, then run the following commands:

set FLASK_APP=password_update.py
flask run
"""

import csv
import string
import socket
from datetime import datetime
from datetime import date
from flask import Flask
from flask import render_template
from flask import request, redirect, session


app = Flask(__name__)  # creates instance of flask class
app.secret_key = 'super_secret_key'


# Must set to local path under /static/ folder
USER_DATABASE = r'C:\Users\Grant\Desktop\School\GitHubProjects\Python\PasswordUpdater\static\UserDatabase.csv'
COMMON_PASSWORDS = r'C:\Users\Grant\Desktop\School\GitHubProjects\Python\PasswordUpdater\static\CommonPassword.txt'
LOGS = r'C:\Users\Grant\Desktop\School\GitHubProjects\Python\PasswordUpdater\static\Logs.csv'


@app.route('/')  # function decorator shows path of URL
def index():
    """
    Loads Index (home) page
    """
    return render_template('index.html', datetime=str(datetime.now()))


@app.route('/signup', methods=['GET', 'POST'])  # function decorator shows path of URL
def signup():
    """
    Loads Sign Up page
    """
    msg = ''  # message that will appear on webpage for password update
    msg_color = 'red'
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')

        # check if one of the common passwords listed in CommonPassword.txt file
        bad_pass = []
        with open(COMMON_PASSWORDS, "r") as p:
            contents = p.read().splitlines()
            for row in contents:
                bad_pass.append(row)
            if password in bad_pass:
                msg = 'Password too common! Please choose another.'
            # check if password meets requirements
            elif len(password) < 6:
                msg = 'Password must be 6 or more characters in length.'
            elif not any(char.isdigit() for char in password):
                msg = 'Password must contain at least 1 number!'
            elif not any(char.isupper() for char in password):
                msg = 'Password must contain at least 1 uppercase character!'
            elif not any(char.islower() for char in password):
                msg = 'Password must contain at least 1 lowercase character!'
            elif not any(char in string.punctuation for char in password):
                msg = 'Password must contain at least 1 special character!'
            else:
                # Open file
                with open(USER_DATABASE, "a") as f:
                    f.writelines(first_name + '\t' + last_name + '\t' + username + '\t' + password + '\n')
                return redirect('/nasa_potd')

    # points to HTML file
    return render_template('signup.html', datetime=str(datetime.now()), msg=msg, msg_color=msg_color)


@app.route('/nasa_potd')  # function decorator shows path of URL
def nasa_potd():
    """
    Loads NASA POTD page
    """
    # points to HTML file
    return render_template('nasa_potd.html', datetime=str(datetime.now()))


@app.route('/login', methods=['POST', 'GET'])  # function decorator shows path of URL
def login():
    """
    Loads Log In page
    """
    msg = ''  # message that will appear on webpage for password update
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open(USER_DATABASE, "r") as f:
            users = []
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                users.append(row)
            count = 0
            for i in users:
                count += 1
                if count == 1:  # skip column headers
                    continue
                if i[2] == username:  # if username is correct
                    if i[3] == password:  # if password is correct
                        session['user'] = username
                        return redirect('/nasa_potd')
                else:  # if the username or password does not match
                    # log failed login attempt
                    with open(LOGS, "a") as log:
                        # get date
                        today = date.today()
                        today = str(today)
                        # get time
                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S")
                        # get IP address
                        hostname = socket.gethostname()
                        ip_add = socket.gethostbyname(hostname)
                        # update log file
                        log.writelines('\n' + today + '\t' + current_time + '\t' + ip_add)
                    msg = 'Wrong username or password'

    # points to HTML file
    return render_template("login.html", datetime=str(datetime.now()), msg=msg)

@app.route('/update_password', methods=['POST', 'GET'])  # function decorator shows path of URL
def update_password():
    """
    Loads password update page
    """
    if 'user' in session:
        # points to HTML file
        current_pass = request.form.get('current_pass')
        new_pass = request.form.get('new_pass')
        retype_pass = request.form.get('retype_pass')
        with open(USER_DATABASE, "r") as f:
            users = []
            msg = ''  # message that will appear on webpage for password update
            msg_color = 'red'
            reader = csv.reader(f, delimiter="\t")
            for row in reader:
                users.append(row)
            count = 0
            for i in users:
                count += 1
                if count == 1:  # skip column headers
                    continue
                if i[2] == session['user']:
                    if i[3] == current_pass:  # if current password is correct

                        # check if one of the common passwords listed in CommonPassword.txt file
                        bad_pass = []
                        with open(COMMON_PASSWORDS, "r") as p:
                            contents = p.read().splitlines()
                            for row in contents:
                                bad_pass.append(row)
                            if new_pass in bad_pass:
                                msg = 'Password too common! Please choose another.'

                            # check if new password meets requirements
                            elif len(new_pass) < 6:
                                msg = 'Password must be 6 or more characters in length.'
                            elif not any(char.isdigit() for char in new_pass):
                                msg = 'Password must contain at least 1 number!'
                            elif not any(char.isupper() for char in new_pass):
                                msg = 'Password must contain at least 1 uppercase character!'
                            elif not any(char.islower() for char in new_pass):
                                msg = 'Password must contain at least 1 lowercase character!'
                            elif not any(char in string.punctuation for char in new_pass):
                                msg = 'Password must contain at least 1 special character!'
                            # make sure passwords match
                            elif new_pass != retype_pass:
                                msg = 'Passwords do not match!'
                            else:
                                # update the password in .csv file
                                update = open(USER_DATABASE, "r")
                                update = ''.join([i for i in update]) \
                                    .replace(current_pass, new_pass)
                                x = open(USER_DATABASE, "w")
                                x.writelines(update)
                                x.close()

                                msg = 'Password updated!'
                                msg_color = 'green'

                    elif current_pass is not None:  # if current password is NOT correct
                        msg = 'Incorrect current password!'

        return render_template("update_password.html", value=session['user'], msg=msg, msg_color=msg_color)

    # if the user is not in the session
    return '<br><h1><center>You are not logged in.</center></h1>'


@app.route('/logout')  # function decorator shows path of URL
def logout():
    """
    Logs out and redirects to Index page
    """
    session.pop('user')  # remove the session from the browser
    return redirect('/login')
