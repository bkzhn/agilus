from api.db import Base


class BaseModel(Base):
    """Base ORM."""

    __abstract__ = True