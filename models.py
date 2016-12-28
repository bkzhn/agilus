from run import db
from sqlalchemy import ForeignKey


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name


class TicketType(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<TicketType %r>' % self.name


class TicketStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<TicketStatus %r>' % self.name


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type_id = db.Column(db.Integer, ForeignKey('ticket_type.id'), nullable=False)
    status_id = db.Column(db.Integer, ForeignKey('ticket_status.id'), nullable=False)
    author = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    assignee = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)


    def __init__(self, title, description, type_id, status_id, author, assignee=None):
        self.title = title
        self.description = description
        self.type_id = type_id
        self.status_id = status_id
        self.author = author
        self.assignee = assignee

    def __repr__(self):
        return '<Ticket %r>' % self.title
