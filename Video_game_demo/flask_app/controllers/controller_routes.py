from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_game import Game

@app.route('/')
def index():
    all_games = Game.get_all()
    return render_template('index.html', all_games=all_games)



## Dashboard

## 404
@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"