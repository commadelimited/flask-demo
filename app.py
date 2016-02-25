from flask import (
    Flask
)

app = Flask('__name__')
app.debug = True


@app.route("/")
def index():
    return """
    <h1>
        Welcome to Sky Adventures!<br />
        The home page says hello!
    </h1>
    """


@app.route("/about-us/")
def schedule():
    return """
    <h1>
        Find out more about Sky Adventures!
    </h1>
    """


@app.route("/packages/")  # converter: int, float, path
def packages():
    return """
    <h1>
        Here's a list of Sky Adventure packages.
    </h1>
    """


@app.route("/packages/<int:id>/<name>/")  # converter: int, float, path
def packages_detail(id, name):
    return """
    <h1>
        {id}!<br />
        {name}.
    </h1>
    """.format(id=id, name=name)


@app.route("/contact/")
@app.route("/contact-sky-adventures/")
def sponsors():
    return """
    <h1>
        Contact Sky Adventures!<br />
    </h1>
    """


# Run application
if __name__ == '__main__':
    app.run(debug=True, port=12345)
