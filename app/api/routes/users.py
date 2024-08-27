"""API."""

from flask import jsonify
from flask import Blueprint

users_api = Blueprint('users_api', __name__)


@users_api.route('/api/v1/users')
def v1_users():
    """Action returns list of users."""
    from api.models.users import User
    users = User.query.all()

    return jsonify({
        'users': [i.serialize for i in users]
    })


@users_api.route('/api/v1/users/<id>')
def v1_user(id):
    """Action returns a user by id."""
    from api.models.users import User
    user = User.query.get_or_404(id)
    return jsonify(user.serialize)
