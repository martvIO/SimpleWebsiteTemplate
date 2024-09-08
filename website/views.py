from flask import Blueprint, render_template
views = Blueprint('views',__name__)

#create the main page
@views.route('/')
def home():
    return render_template("home.html")