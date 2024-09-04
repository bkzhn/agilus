from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session


from api.models.tickets import Ticket, TicketStatus, TicketType
from api.services.base_service import BaseService


class TicketService(BaseService):
    """Ticket Service."""

    def __init__(self, session: Session):
        self.session = session

    def get_tickets(self):
        """Get list of tickets."""
        with self.session() as session:
            query = session.query(Ticket)
            return query.all()

    def get_ticket_by_id(self, id):
        """Get ticket by ID."""
        with self.session() as session:
            try:
                return (
                    session.query(Ticket)
                    .filter(Ticket.id == id)
                    .one()
                )
            except NoResultFound:
                raise Exception('Ticket does not exist')

    def get_ticket_statuses(self):
        """Get list of ticket statuses."""
        with self.session() as session:
            query = session.query(TicketStatus)
            return query.all()

    def get_ticket_status_by_id(self, id):
        """Get ticket status by ID."""
        with self.session() as session:
            try:
                return (
                    session.query(TicketStatus)
                    .filter(TicketStatus.id == id)
                    .one()
                )
            except NoResultFound:
                raise Exception('Ticket status does not exist')

    def get_ticket_types(self):
        """Get list of ticket types."""
        with self.session() as session:
            query = session.query(TicketType)
            return query.all()

    def get_ticket_type_by_id(self, id):
        """Get ticket type by ID."""
        with self.session() as session:
            try:
                return (
                    session.query(TicketType)
                    .filter(TicketType.id == id)
                    .one()
                )
            except NoResultFound:
                raise Exception('Ticket type does not exist')
