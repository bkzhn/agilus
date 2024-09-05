"""API."""
from crypt import methods

from flask import (
    request,
    jsonify,
    Blueprint,
    current_app as app,
)

tickets_api = Blueprint('tickets_api', __name__)


@tickets_api.route('/api/v1/tickets')
def v1_tickets():
    """Action returns list of tickets."""
    tickets = app.container.ticket_service.get_tickets()
    return jsonify({
        'tickets': [i.serialize for i in tickets]
    })


@tickets_api.route('/api/v1/tickets/<id>')
def v1_ticket(id):
    """Action returns a ticket by id."""
    ticket = app.container.ticket_service.get_ticket_by_id(id)
    return jsonify(ticket.serialize)


@tickets_api.route('/api/v1/ticket-types', methods=['GET'])
def v1_ticket_types():
    """Action returns list of ticket types."""
    ticket_types = app.container.ticket_service.get_ticket_types()
    return jsonify({
        'ticket_types': [i.serialize for i in ticket_types]
    })


@tickets_api.route('/api/v1/ticket-types', methods=['POST'])
def v1_create_ticket_type():
    """Action creates new ticket type."""
    data = request.json
    name = data.get('name')
    if not name:
        raise Exception('Invalid name')

    ticket_id = app.container.ticket_service.create_ticket_type(name)
    return jsonify({
        'ticket_id': ticket_id
    })


@tickets_api.route('/api/v1/ticket-types/<id>', methods=['GET'])
def v1_ticket_type(id):
    """Action returns a ticket type by id."""
    ticket_type = app.container.ticket_service.get_ticket_type_by_id(id)
    return jsonify(ticket_type.serialize)


@tickets_api.route('/api/v1/ticket-types/<id>', methods=['DELETE'])
def v1_delete_ticket_type(id):
    """Action deletes ticket type by id."""
    is_deleted = app.container.ticket_service.delete_ticket_type_by_id(id)
    return jsonify({
        'ticket_type_id': id,
        'is_deleted': is_deleted,
    })


@tickets_api.route('/api/v1/ticket-statuses', methods=['GET'])
def v1_ticket_statuses():
    """Action returns list of ticket statuses."""
    ticket_statuses = app.container.ticket_service.get_ticket_statuses()
    return jsonify({
        'ticket_statuses': [i.serialize for i in ticket_statuses]
    })


@tickets_api.route('/api/v1/ticket-statuses', methods=['POST'])
def v1_create_ticket_status():
    """Action creates new ticket status."""
    data = request.json
    name = data.get('name')
    if not name:
        raise Exception('Invalid name')

    ticket_status_id = app.container.ticket_service.create_ticket_status(name)
    return jsonify({
        'ticket_status_id': ticket_status_id
    })


@tickets_api.route('/api/v1/ticket-statuses/<id>', methods=['DELETE'])
def v1_delete_ticket_status(id):
    """Action deletes ticket status by ID."""
    is_deleted = app.container.ticket_service.delete_ticket_status_by_id(id)
    return jsonify({
        'ticket_status_id': id,
        'is_deleted': is_deleted,
    })


@tickets_api.route('/api/v1/ticket-statuses/<id>')
def v1_ticket_status(id):
    """Action returns a ticket status by id."""
    ticket_status = app.container.ticket_service.get_ticket_status_by_id(id)
    return jsonify(ticket_status.serialize)

