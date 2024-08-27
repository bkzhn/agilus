"""Models."""

from sqlalchemy import ForeignKey

from api.application import db


class TicketType(db.Model):
    """TicketType."""

    __tablename__ = 'ticket_types'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        """Constructor."""
        self.name = name

    def __repr__(self):
        """String representation."""
        return '<TicketType %r>' % self.name

    @property
    def serialize(self):
        """Dictionary representation."""
        return {
            'name': self.name,
        }


class TicketStatus(db.Model):
    """TicketStatus."""

    __tablename__ = 'ticket_statuses'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        """Constructor."""
        self.name = name

    def __repr__(self):
        """String representation."""
        return '<TicketStatus %r>' % self.name

    @property
    def serialize(self):
        """Dictionary representation."""
        return {
            'name': self.name,
        }


class Ticket(db.Model):
    """Ticket."""

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type_id = db.Column(db.Integer, ForeignKey('ticket_types.id'), nullable=False)
    status_id = db.Column(db.Integer, ForeignKey('ticket_statuses.id'), nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    assignee_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=True)

    def __init__(self, title, description, type_id, status_id, author_id, assignee_id=None):
        """Constructor."""
        self.title = title
        self.description = description
        self.type_id = type_id
        self.status_id = status_id
        self.author_id = author_id
        self.assignee_id = assignee_id

    def __repr__(self):
        """String representation."""
        return '<Ticket %r>' % self.title

    @property
    def serialize(self):
        """Dictionary representation."""
        return {
            'title': self.title,
            'description': self.description,
            'type_id': self.type_id,
            'status_id': self.status_id,
            'author_id': self.author_id,
            'assignee_id': self.assignee_id
        }
