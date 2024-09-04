from api.config import Config
from api.db import Database
from api.services.user_service import UserService


class Container:
    """DI container."""
    db = Database(dsn=Config.SQLALCHEMY_DATABASE_URI)

    user_service = UserService(session=db.session)
