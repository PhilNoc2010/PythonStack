from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_dojos import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/ninja/new')
def ninja_new():
    all_dojos = Dojo.get_all()
    return render_template('ninja_new.html', all_dojos=all_dojos)

@app.route('/ninja/create', methods=['POST'])
def ninja_create():
    new_ninja = Ninja.add_one(request.form)
    ## stuggling with how to capture the dojo ID and pass it into the re-direct
    return redirect ('/ninja/<int:id>/show')

@app.route('/ninja/<int:id>/show')
def ninja_show(id):
    ninjas = Ninja.get_all_by_dojo({'dojo_id': id})
    dojo = Dojo.get_one({'id': id})
    return render_template('dojo_show.html', ninjas=ninjas, dojo=dojo)