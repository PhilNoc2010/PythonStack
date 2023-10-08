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
    User.add_one(request.form)
    return redirect('/')

