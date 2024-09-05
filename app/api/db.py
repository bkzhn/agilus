"""DB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    Session,
    sessionmaker,
    scoped_session,
)

Base = declarative_base()

class Database:
    """Database."""

    def __init__(self, dsn: str) -> None:
        """Create Database instance."""
        self.engine = create_engine(dsn, echo=False)
        self._scoped_session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
            )
        )

    def session(self) -> scoped_session:
        """Get SQLAlchemy session."""
        session: Session = self._scoped_session
        try:
            return session
        except Exception:
            session.rollback()
            raise
