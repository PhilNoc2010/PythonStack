from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Your Princess is in another castle"

@app.route('/')
def click_button():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] = session['counter'] + 1
    return render_template("index.html", counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/double_count')
def double_count():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] = session['counter'] + 1
    return redirect('/')

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.