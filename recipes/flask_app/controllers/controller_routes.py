from flask import render_template, session, redirect
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe

@app.route('/')
def index():
    return render_template("index.html")

##dashboard
@app.route('/dashboard')
def dashboard():
    if "user_id" in session:
        all_recipes = Recipe.get_all_joined_recipes()
        print(all_recipes)
        return render_template("dashboard.html", all_recipes=all_recipes)
    return redirect('/')

#404
@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"