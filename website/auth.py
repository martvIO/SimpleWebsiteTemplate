from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import *  # Import all models
import os

# Create a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Route for login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        # get the input values
        name = request.form.get('name')
        password = request.form.get('password')
        
        # Check if the user exists in the database
        user = dp()
        res = user.CheckUser(name)
        print(res)
        
        # Verify password and redirect to home page if successful
        for i in res:
            if i == password:
                flash('Login successfully!', category='success')
                session['user'] = name
                return redirect(url_for('views.home'))
            
        # if the login wasn't successful
        flash('username or password are incorrect!')
    return render_template("login.html")
    

# Route for logout
@auth.route('/logout')
def logout():
    session['user'] = None
    return "<p>Logout</p>"

# Route for sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Get form data
        data = request.form
        name = data.get('firstName')
        email = data.get('email')
        password = data.get('password1')

        # Validate input data
        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(password) < 8:
            flash('Password must be greater than 8 characters.', category='error')    
        else:
            # Create new user
            user = dp()
            user.CreateUser(name, email, password)
            flash('Account created!', category='success')
            return redirect(url_for('views.home')) # return to the default home page

    # Render the sign-up page
    return render_template("sign_up.html")