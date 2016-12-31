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


@app.route('/ticket/<id>')
def ticket(id):
    from models import Ticket
    ticket = Ticket.query.get_or_404(id)
    return jsonify(ticket.serialize)


if __name__ == '__main__':
    app.run()
