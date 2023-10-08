from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_dojos import Dojo

# /table_name/new (Display Route)
# /table_name/create (Action Route)
# /table_name/<int:id>
# /table_name/<int:id>/edit
# /table_name/<int:id>/update
# /table_name/<int:id>/delete

@app.route('/dojos/new')
def dojo_new():
    return render_template('dojo_new.html')

@app.route('/dojos/create/', methods=['POST'])
def dojo_create():
    id = Dojo.add_one(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojo_show(id):
    dojo = Dojo.get_one({'id': id})
    return render_template('dojo_show.html', dojo=dojo)

@app.route('/dojos/<int:id>/edit')
def dojo_edit(id):
    dojo = Dojo.get_one({'id': id})
    return render_template('dojo_edit.html', dojo=dojo)

@app.route('/dojos/<int:id>/update', methods=["POST"])
def dojo_update(id):
    Dojo.update_one(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>/delete')
def dojo_delete(id):
    Dojo.delete_one({'id' : id})
    return redirect('/')