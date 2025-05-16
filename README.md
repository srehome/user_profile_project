# user_profile_project

## ABOUT THE PROJECT:

My User Profile Project uses Python Flask server-side with a MongoDB database.
This means my project must be run in a python virtual environment.
If you know how to install one yourself and can run my project in it, by all means.
However, if you do not know, I have included those instructions below.
As long as you have a MongoDB server running, the database should instantiate itself when you register your first user.

IMPORTANT NOTE: My HTML pages have errors due to the Jinja Flask notation: {{ url_for('static', filename='...') }} that I use to locate my static files, but that is the best practice I could find to use with a Flask application.

## HOW TO INSTALL & RUN:

### Install a Virtual Environment
1. Make sure your computer has python and pip installed. To check, open a command prompt and type:
    * python3 --version
    * pip --version
2. Make sure your VSCode has the python extensions installed (they might all be installed at once):
    * Python
    * Pylance
    * Python Debugger
3. Navigate into this project directory & enter the code below in the terminal to create a virtual environment for python:
    * Windows: Manual install:
        1. py -m venv venv
    * Mac/Unix: Manual install:
        1. python3 -m pip install virtualenv
        2. python3 -m virtualenv venv
4. Activate your virtual environment:
    * VSCode: simply open a brand new terminal, and it will activate
        * NOTE: If it is working, you will see (.venv) before your terminal path
    * Windows Manual activation:
        * venv\Scripts\activate.bat
    * Unix/MacOS Manual activation:
        * source venv/bin/activate

### Install the Packages
* With the virtual environment active, enter this in the terminal to install all packages:
    * pip install -r requirements.txt

### Run the App
* flask --app server/main run
* In your browser, enter:
    * http://127.0.0.1:5000