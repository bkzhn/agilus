"""API."""

from flask import jsonify
from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/api/v1/tickets')
def v1_tickets():
    """Action returns list of tickets."""
    from models import Ticket
    tickets = Ticket.query.all()

    return jsonify({
        'tickets': [i.serialize for i in tickets]
    })


@api.route('/api/v1/ticket/<id>')
def v1_ticket(id):
    """Action returns a ticket by id."""
    from models import Ticket
    ticket = Ticket.query.get_or_404(id)
    return jsonify(ticket.serialize)
