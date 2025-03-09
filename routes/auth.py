from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import users_collection

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    if 
    return render_template('main.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password =  request.form['password']

        exist = users_collection.find_one({"email": email})
        if exist:
            return render_template('register.html', error="Email already exists!")
        else:
            hash_password = generate_password_hash(password)
            users_collection.insert_one({
                "username": username,
                "email": email,
                "password": hash_password
            })
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = users_collection.find_one({"email": email})
        if not user:
            return render_template('login.html', error="Email not found!")
        elif not check_password_hash(user['password'], password):
            return render_template('login.html', error="Incorrect password!")
        else:
            return render_template('login.html', success="Logged in successfully!")
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('/register'))

