from flask import (
    Flask
)

app = Flask('__name__')
app.debug = True

@app.route("/")
def homepage():
    return """
    <h1>
        Welcome to PyTennessee!<br />
        The home page says hello!
    </h1>
    """

@app.route("/news/")
def news():
    return """
    <h1>
        PyTennessee 2015!<br />
        All the news that's fit to print.
    </h1>
    """

@app.route("/schedule/")
def schedule():
    return """
    <h1>
        PyTennessee Conference Schedule!<br />
        Tough decisions all around.<br />
        But you, you chose wisely.
    </h1>
    """

@app.route("/sponsors/")
def sponsors():
    return """
    <h1>
        PyTennessee Sponsors!<br />
        The ones with the bucks<br />
        And the bags and stickers and shirts!
    </h1>
    """

@app.route("/conduct/")
def conduct():
    return """
    <h1>
        PyTennessee Rules of the road!<br />
        Be excellent to each other.<br />
    </h1>
    """

# Run application
if __name__ == '__main__':
    app.run(debug=True, port=12345)