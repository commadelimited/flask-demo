from flask import (
    Flask,
    g,
    render_template,
    request,
)

app = Flask('__name__')
app.debug = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about-us/")
def about():
    return render_template('about.html')


@app.route("/packages/")  # converter: int, float, path
def packages():
    return render_template('packages.html')


@app.route("/packages/<int:id>/<name>/")  # converter: int, float, path
def package_details(id, name):
    context = {
        'id': id,
        'name': name,
    }
    return render_template('packages-details.html', context=context)


@app.route("/contact-sky-adventures/")
@app.route("/contact/")
def contact():
    return render_template('contact.html')


# Run application
if __name__ == '__main__':
    app.run(debug=True, port=12345)
