from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/play')
def draw_boxes():
    return render_template("index.html", times=3, color="blue")

@app.route('/play/<int:times>')
def draw_boxes_more(times):
    return render_template("index.html", times=times, color="blue")

@app.route('/play/<string:color>')
def draw_boxes_color(color):
    return render_template("index.html", color=color)

@app.route('/play/<int:times>/<color>')
def draw_boxes_more_color(times, color):
    return render_template("index.html", times=times, color=color)

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

