from flask import (
    Flask,
    g,
    render_template,
    request,
)
from packages import packages_blueprint

app = Flask('__name__')
app.debug = True

app.register_blueprint(packages_blueprint, url_prefix='/packages')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about-us/")
def about():
    return render_template('about.html')


@app.route("/contact-sky-adventures/")
@app.route("/contact/")
def contact():
    return render_template('contact.html')


@app.before_request
def before_request():
    if 'packages' in request.endpoint:
        g.active = 'packages'
    else:
        g.active = request.endpoint
    print g.active


# Run application
if __name__ == '__main__':
    app.run(debug=True, port=12345)
