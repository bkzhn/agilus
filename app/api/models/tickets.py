"""Models."""

from sqlalchemy import ForeignKey, Integer, String, Column, Text

from api.models.base import BaseModel
# from api.application import db


class TicketType(BaseModel):
    """TicketType."""

    __tablename__ = 'ticket_types'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)

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
            'id': self.id,
            'name': self.name,
        }


class TicketStatus(BaseModel):
    """TicketStatus."""

    __tablename__ = 'ticket_statuses'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)

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
            'id': self.id,
            'name': self.name,
        }


class Ticket(BaseModel):
    """Ticket."""

    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    type_id = Column(Integer, ForeignKey('ticket_types.id'), nullable=False)
    status_id = Column(Integer, ForeignKey('ticket_statuses.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    assignee_id = Column(Integer, ForeignKey('users.id'), nullable=True)

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
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'type_id': self.type_id,
            'status_id': self.status_id,
            'author_id': self.author_id,
            'assignee_id': self.assignee_id
        }
