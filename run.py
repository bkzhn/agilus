from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Agilus'

if __name__ == '__main__':
    app.run()
