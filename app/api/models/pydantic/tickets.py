from pydantic import BaseModel


class CreateTicketType(BaseModel):
    name: str

class CreateTicketStatus(BaseModel):
    name: str

class CreateTicket(BaseModel):
    title: str
    description: str
    type_id: int
    status_id: int
    author_id: int
    assignee_id: int | None = None
