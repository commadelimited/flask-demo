from flask import (
    Blueprint,
    render_template,
)

packages_blueprint = Blueprint('packages_blueprint', __name__)


@packages_blueprint.route("/")  # converter: int, float, path
def packages():
    return render_template('packages.html')


@packages_blueprint.route("/<int:id>/<name>/")  # converter: int, float, path
def package_details(id, name):
    context = {
        'id': id,
        'name': name,
    }
    return render_template('packages-details.html', context=context)
