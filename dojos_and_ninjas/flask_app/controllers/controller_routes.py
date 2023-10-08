from flask import render_template
from flask_app import app
from flask_app.models.model_dojos import Dojo

@app.route('/')
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)

##dashboard

##404
@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"
