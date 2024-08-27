"""Models."""

from api.application import db


class User(db.Model):
    """User."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        """Constructor."""
        self.name = name

    def __repr__(self):
        """String representation."""
        return '<User %r>' % self.name

    @property
    def serialize(self):
        """Dictionary representation."""
        return {
            'name': self.name,
        }
