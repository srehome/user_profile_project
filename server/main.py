import os
from os.path import join, dirname, realpath
from . import app
from . import models
from . import views

# Set a secret key for securely signing the session data
app.secret_key = os.urandom(12)

UPLOAD_FOLDER = '../client/static\\images'
UPLOADS_PATH = join(dirname(realpath(__file__)), UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_PATH'] = UPLOADS_PATH
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)