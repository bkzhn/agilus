"""Models."""

from sqlalchemy import Column, Integer, String

from api.models.orm.base import BaseModel


class User(BaseModel):
    """User."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(100), nullable=False)

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
            'id': self.id,
            'name': self.name,
        }
