from flask import (
    Flask
)

app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return '<img src="/static/img/nick.png" />'


# Run application
if __name__ == '__main__':
    app.run(debug=True, port=12345)
