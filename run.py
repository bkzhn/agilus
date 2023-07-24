"""Main."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.application import app

if __name__ == '__main__':
    app.run(host='0.0.0.0')
