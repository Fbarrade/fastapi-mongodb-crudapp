from pydantic import BaseModel, EmailStr, Field, HttpUrl, validator
import uuid
from typing import Optional
class Organizer(BaseModel):
    organizer_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    organizer_name: str
    contact_email: EmailStr
    contact_phone: str
    organizer_description: Optional[str] = None
    website_url: Optional[HttpUrl] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class UpdateOrganizer(BaseModel):
    organizer_name: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    contact_phone: Optional[str] = None
    organizer_description: Optional[str] = None
    website_url: Optional[HttpUrl] = None

    @validator("contact_phone")
    def phone_length_check(cls, contact_phone):
        if contact_phone and not (7 <= len(contact_phone) <= 15):
            raise ValueError("Phone number must be between 7 and 15 characters.")
        return contact_phone

    class Config:
        allow_population_by_field_name = True
