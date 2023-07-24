"""API."""

from flask import jsonify
from flask import Blueprint

tickets_api = Blueprint('api', __name__)


@tickets_api.route('/api/v1/tickets')
def v1_tickets():
    """Action returns list of tickets."""
    from api.models import Ticket
    tickets = Ticket.query.all()

    return jsonify({
        'tickets': [i.serialize for i in tickets]
    })


@tickets_api.route('/api/v1/ticket/<id>')
def v1_ticket(id):
    """Action returns a ticket by id."""
    from api.models import Ticket
    ticket = Ticket.query.get_or_404(id)
    return jsonify(ticket.serialize)
