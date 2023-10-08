from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.model_game import Game
from flask_app.models.model_company import Company

# /table_name/id/action
# /table_name/new (Display Route)
# /table_name/create (Action Route)
# /table_name/<int:id>
# /table_name/<int:id>/edit
# /table_name/<int:id>/update
# /table_name/<int:id>/delete

# display route to show the form to enter a new game
@app.route('/games/new')
def game_new():
    all_companys = Company.get_all()
    return render_template('game_new.html', all_companys=all_companys)

# Action route to add a new game to the database
@app.route('/games/create/', methods=["POST"])
def game_create():
    ##validate the form
    ### insert logic to add game here
    Game.add_one(request.form)
    return redirect('/')

# display route to display the game info
@app.route('/games/<int:id>')
def game_show(id):
    ### get the game by ID and pass instance to the HTML form
    game = Game.get_one({'id' : id})
    return render_template('game_show.html', game=game)

# display route to show the game edit form
@app.route('/games/<int:id>/edit')
def game_edit(id):
    ### get the game by ID and pass instance to the HTML form
    return render_template('game_edit.html')

## Action route to process form from the edit route
@app.route('/games/<int:id>/update', methods=["POST"])
def game_update(id):
    ## update the game information for the incoming ID
    return redirect('/')

# Action route to remove the selected game from the database based on the incoming ID
@app.route('/games/<int:id>/delete', methods=["POST"])
def game_delete(id):
    # logic to remove game from database by incoming ID
    Game.remove_game({'id' : id})
    return redirect('/')