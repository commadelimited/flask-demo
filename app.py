from flask import (
    Flask
)

# app = Flask('__name__')
app = Flask(__name__)
app.debug = True


@app.route("/")
def hello():
    return "Hello World!"


# Run application
if __name__ == '__main__':
    # from os import environs
    # app.run(debug=False, port=environ.get("PORT", 5000), processes=2)
    app.run(debug=True, port=12345)