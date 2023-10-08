from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_users import User

# /table_name/new (Display Route)
# /table_name/create (Action Route)
# /table_name/<int:id>
# /table_name/<int:id>/edit
# /table_name/<int:id>/update
# /table_name/<int:id>/delete

@app.route('/users/new')
def user_new():
    return render_template('user_new.html')

@app.route('/users/create/', methods=['POST'])
def user_create():
    id = User.add_one(request.form)
    # return redirect('users/<str:id>', id=id)
    return redirect('/')

@app.route('/users/<int:id>')
def user_show(id):
    user = User.get_one({'id': id})
    return render_template('user_show.html', user=user)

@app.route('/users/<int:id>/edit')
def user_edit(id):
    user = User.get_one({'id': id})
    return render_template('user_edit.html', user=user)

@app.route('/users/<int:id>/update', methods=["POST"])
def user_update(id):
    User.update_one(request.form)
    return redirect('/')

@app.route('/users/<int:id>/delete')
def user_delete(id):
    User.delete_one({'id' : id})
    return redirect('/')
