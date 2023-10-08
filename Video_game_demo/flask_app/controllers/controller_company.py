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

# display route to show the form to enter a new company
@app.route('/companys/new')
def company_new():
    return render_template('company_new.html')

# Action route to add a new company to the database
@app.route('/companys/create', methods=["POST"])
def company_create():
    ##validate the form
    ### insert logic to add company here
    Company.add_one(request.form)
    return redirect('/')

# display route to display the company info
@app.route('/companys/<int:id>')
def company_show(id):
    ### get the company by ID and pass instance to the HTML form
    company = Company.get_one({'id' : id})
    return render_template('company_show.html', company=company)

# display route to show the company edit form
@app.route('/companys/<int:id>/edit')
def company_edit(id):
    ### get the company by ID and pass instance to the HTML form
    return render_template('company_edit.html')

## Action route to process form from the edit route
@app.route('/companys/<int:id>/update', methods=["POST"])
def company_update(id):
    ## update the company information for the incoming ID
    return redirect('/')

# Action route to remove the selected company from the database based on the incoming ID
@app.route('/companys/<int:id>/delete', methods=["POST"])
def company_delete(id):
    # logic to remove company from database by incoming ID
    Company.remove_company({'id' : id})
    return redirect('/')