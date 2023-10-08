from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.model_users import User

@app.route('/')
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)

##dashboard

##404
@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"
