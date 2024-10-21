from pydantic import BaseModel, Field,  validator
import uuid
from typing import Optional
class Ticket(BaseModel):
    ticket_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    event_id: str  # Foreign key to Events collection
    ticket_type: str
    ticket_price: float
    availability: int
    sold: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class UpdateTicket(BaseModel):
    event_id: Optional[str] = None
    ticket_type: Optional[str] = None
    ticket_price: Optional[float] = None
    availability: Optional[int] = None
    sold: Optional[int] = None

    @validator('ticket_price')
    def price_check(cls, ticket_price):
        if ticket_price is not None and ticket_price < 0:
            raise ValueError('Ticket price must be non-negative.')
        return ticket_price

    @validator('availability', 'sold')
    def availability_and_sold_check(cls, value):
        if value is not None and value < 0:
            raise ValueError('Availability and sold tickets must be non-negative.')
        return value

    class Config:
        allow_population_by_field_name = True
