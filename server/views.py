from flask import Flask, session, redirect, url_for, request, render_template, jsonify, flash
from datetime import datetime
from . import app
from . import models
from . import db
from pydantic import ValidationError
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
import os

@app.route("/")
def home():
    # Check if 'username' is in session
    if 'username' in session:
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('login'))

# Route to set session data
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # check user sign-in credentials
        user = db.users_collection.find_one({"username": request.form['username']})
        if not user:
            flash('No user by that username')
            return redirect(url_for('login'))
        
        if not check_password_hash(user['password'], request.form['password']):
            flash('Incorrect password')
            return redirect(url_for('login'))

        # Set user-specific session data
        session['username'] = request.form['username']

        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/register_user', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
        try:
            # Check for existing user with this username
            existing_user = db.users_collection.find_one({"username": request.form['username']})
            if existing_user:
                flash("Username not unique!")
                return redirect(url_for('register_user'))
            
            # Validate request data
            user = models.UserModel(**request.form)
            db.users_collection.insert_one(user.model_dump())

            return redirect(url_for('login'))
        except ValidationError as err:
            for error in err.errors():
                flash(error)
            return redirect(url_for('register_user'))
    return render_template('register.html')

# Route to access session data
@app.route('/profile')
def profile():
    # Check if 'username' is in session
    if 'username' in session:
        user = db.users_collection.find_one({"username": session['username']})
        return render_template('profile.html', user=user)
    else:
        return "You are not logged in!"

# Route to clear session data
@app.route('/logout')
def logout():
    # Clear the session
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/update_profile', methods=['GET','POST'])
def update_profile():
    if 'username' in session:
        if request.method == 'POST':
            try:
                # Check for existing user with this username
                if request.form['username'] != session['username']:
                    existing_user = db.users_collection.find_one({"username": request.form['username']})
                    if existing_user:
                        flash("Username not unique!")
                        return redirect(url_for('update_profile'))
                
                # Validate request data
                current_user = db.users_collection.find_one({"username": session['username']})
                profile_path = current_user['profile_picture']
                user = models.UserModel(**request.form)
                db.users_collection.update_one({"_id": current_user['_id']}, {"$set": user.model_dump()})
                db.users_collection.update_one({"_id": current_user['_id']}, {"$set": {'profile_picture': profile_path}})
                
                # Reset the session for new username
                session['username'] = request.form['username']
                return_user = db.users_collection.find_one({"username": session['username']})
                return render_template('profile.html', user=return_user)

            except ValidationError as err:
                for error in err.errors():
                    flash(error)
                return redirect(url_for('update_profile'))

        current_user = db.users_collection.find_one({"username": session['username']})
        return render_template('update.html', user=current_user)
    else:
        return "You are not logged in!"

@app.route("/upload_profile_picture", methods=['POST'])
def upload_profile_picture():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'profile_picture' not in request.files:
            flash('No file part')
            return redirect(url_for('profile'))
        file = request.files['profile_picture']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('profile'))
        allowed_file = '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
        if file and allowed_file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            current_user = db.users_collection.find_one({"username": session['username']})
            db.users_collection.update_one({"_id": current_user['_id']}, {"$set": {'profile_picture': os.path.join('images/', filename)}})
            return redirect(url_for('profile'))
