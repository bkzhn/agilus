"""DB"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, Session, sessionmaker

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
