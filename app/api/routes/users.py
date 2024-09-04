"""API."""

from flask import jsonify
from flask import Blueprint
from flask import current_app as app

users_api = Blueprint('users_api', __name__)


@users_api.route('/api/v1/users')
def v1_users():
    """Action returns list of users."""
    users = app.container.user_service.get_users()
    return jsonify({
        'users': [i.serialize for i in users]
    })


@users_api.route('/api/v1/users/<id>')
def v1_user(id):
    """Action returns a user by id."""
    user = app.container.user_service.get_user_by_id(id)
    return jsonify(user.serialize)