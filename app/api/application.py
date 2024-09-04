"""Application"""

from flask import Flask

from api.container import Container
from api.routes.tickets import tickets_api
from api.routes.users import users_api



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

    return app


container = create_container()
app = create_app(container)

@app.route('/')
def index():
    """Index page."""
    return 'Agilus'


@app.route('/healthcheck')
def healthcheck():
    """Healthcheck endpoint."""
    return 'OK'
