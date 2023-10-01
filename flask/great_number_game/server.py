from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Your Princess is in another castle"

@app.route('/')
def click_button():
    if 'answer' not in session:
        session['answer'] = random.randint(1,100)
    if 'hintcolor' not in session:
        session['hintcolor'] = "orange"
    return render_template("index.html", randomint = session['answer'])

@app.route('/check_guess', methods=['POST'])
def check_guess():
    if 'guesscount' not in session:
        session['guesscount']=0
    guess = int(request.form['guess'])
    session['guesscount'] = session['guesscount'] + 1
    if (guess > 100 or guess < 1 ):
        session['status'] = "your answer was invalid"
        session['hintcolor'] = 'purple'
    elif (guess > session['answer']):  #user guess a number higher than the answer
        session['status'] = "your answer was too high"
        session['hintcolor'] = 'red'
    elif (guess < session['answer']):  #user guessed a number too low
        session['status'] = "your answer was too low"
        session['hintcolor'] = 'blue'
    else:
        session['status'] = "your answer was correct"
        session['hintcolor'] = "green"
        session['resultvisible'] = "visible"
    return redirect('/')

@app.route('/reset_game')
def reset_game():
    session.pop('answer')
    session['guesscount'] = 0
    session['resultvisible'] = "hidden"
    return redirect('/')

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.