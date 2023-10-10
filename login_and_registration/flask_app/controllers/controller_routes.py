from flask import render_template, session, redirect
from flask_app import app
from flask_app.models.model_user import User

@app.route('/')
def index():
    return render_template("index.html")

##dashboard
@app.route('/dashboard')
def dashboard():
    if session:
        return render_template("dashboard.html")
    return redirect('/')

##404
@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"