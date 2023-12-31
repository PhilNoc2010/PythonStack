from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>')
@app.route('/<int:x>/<int:y>/<color0>/<color1>')             # The "@" decorator associates this route with the function immediately following
def draw_boxes(x=8,y=0, color0="red", color1="black"):
    if (y == 0):
        y = x
    return render_template("index.html",  x=x, y=y, color0=color0, color1=color1)

@app.route("/<path:path>")
def default_route(path):
    return f"you tried to go to {path} but there's nothing here yet"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.