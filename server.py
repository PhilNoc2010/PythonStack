from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "Your Princess is in another castle"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.