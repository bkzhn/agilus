"""Application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

from api.routes.tickets import tickets_api


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('api.config.Config')

    app.register_blueprint(tickets_api)

    db.init_app(app)

    return app


app = create_app()
# migrate = Migrate(app, db)

@app.route('/')
def index():
    """Index page."""
    return 'Agilus'
