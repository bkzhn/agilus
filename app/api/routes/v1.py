from flask import Blueprint


from api.routes.users import users_api
from api.routes.tickets import tickets_api

v1_api = Blueprint('v1_api', __name__, url_prefix='/api/v1/')
v1_api.register_blueprint(users_api)
v1_api.register_blueprint(tickets_api)
