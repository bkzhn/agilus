from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Agilus'


@app.route('/tickets')
def tickets():
    from models import Ticket
    tickets = Ticket.query.all()

    return jsonify({
        'tickets': [i.serialize for i in tickets]
    })


if __name__ == '__main__':
    app.run()
