"""API."""

from flask import jsonify
from flask import Blueprint

tickets_api = Blueprint('tickets_api', __name__)


@tickets_api.route('/api/v1/tickets')
def v1_tickets():
    """Action returns list of tickets."""
    from api.models.tickets import Ticket
    tickets = Ticket.query.all()

    return jsonify({
        'tickets': [i.serialize for i in tickets]
    })


@tickets_api.route('/api/v1/tickets/<id>')
def v1_ticket(id):
    """Action returns a ticket by id."""
    from api.models.tickets import Ticket
    ticket = Ticket.query.get_or_404(id)
    return jsonify(ticket.serialize)


@tickets_api.route('/api/v1/ticket-types')
def v1_ticket_types():
    """Action returns list of ticket types."""
    from api.models.tickets import TicketType
    ticket_types = TicketType.query.all()

    return jsonify({
        'ticket_types': [i.serialize for i in ticket_types]
    })


@tickets_api.route('/api/v1/ticket-types/<id>')
def v1_ticket_type(id):
    """Action returns a ticket type by id."""
    from api.models.tickets import TicketType
    ticket_type = TicketType.query.get_or_404(id)
    return jsonify(ticket_type.serialize)


@tickets_api.route('/api/v1/ticket-statuses')
def v1_ticket_statuses():
    """Action returns list of ticket statuses."""
    from api.models.tickets import TicketStatus
    ticket_statuses = TicketStatus.query.all()

    return jsonify({
        'ticket_statuses': [i.serialize for i in ticket_statuses]
    })


@tickets_api.route('/api/v1/ticket-statuses/<id>')
def v1_ticket_status(id):
    """Action returns a ticket status by id."""
    from api.models.tickets import TicketStatus
    ticket_status = TicketStatus.query.get_or_404(id)
    return jsonify(ticket_status.serialize)


