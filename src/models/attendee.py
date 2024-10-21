from pydantic import BaseModel, EmailStr, Field,  validator
import uuid
from typing import Optional
class Attendee(BaseModel):
    attendee_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    event_id: str  # Foreign key to Events collection
    ticket_id: str  # Foreign key to Tickets collection
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    payment_id: str  # Foreign key to Payments collection

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class UpdateAttendee(BaseModel):
    event_id: Optional[str] = None
    ticket_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    payment_id: Optional[str] = None

    @validator("phone")
    def phone_length_check(cls, phone):
        if phone and not (7 <= len(phone) <= 15):
            raise ValueError("Phone number must be between 7 and 15 characters.")
        return phone

    class Config:
        allow_population_by_field_name = True
