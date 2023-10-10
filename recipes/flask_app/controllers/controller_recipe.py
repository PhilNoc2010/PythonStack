from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_recipe import Recipe

@app.route('/recipe/new')
def recipe_new():
    if session:
        return render_template("add_recipe.html")
    return redirect('/')

@app.route('/recipe/create', methods=['POST'])
def recipe_add():
    if not Recipe.validate_recipe(request.form):
         return redirect('/recipe/new')

    data = {** request.form}
    ## capture the logged in user to store as the creator of the recipe
    data['user_id'] = session['user_id']
    data['under_30_min'] = int(request.form['under_30_min'])
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/update', methods=['POST'])
def recipe_update():
    if not Recipe.validate_recipe(request.form):
         id = str(request.form['id'])
         return redirect(f'/recipe/edit/{id}')

    data = {** request.form}
    ## capture the logged in user to store as the creator of the recipe
    data['user_id'] = session['user_id']
    data['under_30_min'] = int(request.form['under_30_min'])
    Recipe.update_recipe(data)
    return redirect('/dashboard')

@app.route('/recipe/show/<int:id>')
def recipe_show(id):
    if session:
        recipe = Recipe.get_one_recipe_joined({'id': id})
        return render_template("show_recipe.html", recipe=recipe)
    return redirect('/')

@app.route('/recipe/edit/<int:id>')
def recipe_edit(id):
    recipe = Recipe.get_one_recipe_joined({'id': id})
    if "user_id" in session and recipe.user_id == session['user_id']:
        return render_template("edit_recipe.html", recipe=recipe)
    return redirect('/')

@app.route('/recipe/delete/<int:id>')
def recipe_delete(id):
    recipe = Recipe.delete_one_recipe({'id': id})
    return redirect('/dashboard')
