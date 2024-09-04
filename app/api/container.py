from api.config import Config
from api.db import Database
from api.services.user_service import UserService
from api.services.ticket_service import TicketService


class Container:
    """DI container."""
    db = Database(dsn=Config.SQLALCHEMY_DATABASE_URI)

    db_session = db.session()

    user_service = UserService(session=db_session)

    ticket_service = TicketService(session=db_session)
