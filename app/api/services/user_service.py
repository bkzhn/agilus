from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from api.models.orm.users import User
from api.services.base_service import BaseService


class UserService(BaseService):
    """User Service."""

    def __init__(self, session: Session):
        self.session = session

    def get_users(self):
        """Get list of users."""
        with self.session() as session:
            query = session.query(User)
            return query.all()

    def get_user_by_id(self, id):
        """Get user by ID."""
        with self.session() as session:
            try:
                return (
                    session.query(User)
                    .filter(User.id == id)
                    .one()
                )
            except NoResultFound:
                raise Exception('User does not exist')
