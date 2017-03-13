"""Main."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import api

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(api)

db = SQLAlchemy(app)


@app.route('/')
def index():
    """Index page."""
    return 'Agilus'


if __name__ == '__main__':
    app.run()
