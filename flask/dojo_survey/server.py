from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Your Princess is in another castle"

@app.route('/')
def open_form():
    ##clear session variable when a new form is opened
    if 'name' in session:
        session.clear
    return render_template ("index.html")

@app.route('/process', methods=['POST'])
def process_form():
    print(request.form)
    # session = request.form
    # print (session)
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    session["operating_system"] = request.form["operating_system"]
    session["smartphone"] = request.form.getlist('smartphone')
    print (session)
    return redirect("/results")

@app.route ('/results')
def show_results():
    return render_template ("result.html")

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.