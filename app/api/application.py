"""Application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.testing.plugin.plugin_base import config

# from flask_migrate import Migrate

from api.config import Config
from api.container import Container
from api.db import Database
from api.routes.tickets import tickets_api
from api.routes.users import users_api
from api.services.user_service import UserService


#db = SQLAlchemy()

def create_container():
    """Create DI container."""

    container = Container()

    return container

def create_app(container: Container):
    app = Flask(__name__)
    app.container = container
    app.config.from_object('api.config.Config')

    app.register_blueprint(users_api)
    app.register_blueprint(tickets_api)

    # db.init_app(app)

    return app


container = create_container()
app = create_app(container)
# migrate = Migrate(app, db)

@app.route('/')
def index():
    """Index page."""
    return 'Agilus'


@app.route('/healthcheck')
def healthcheck():
    """Healthcheck endpoint."""
    return 'OK'
