import uuid
from typing import Optional
from pydantic.networks import EmailStr
from pydantic import BaseModel, EmailStr, Field, HttpUrl, validator

from datetime import datetime
class Event(BaseModel):
    _id: str = Field(default_factory=uuid.uuid4, alias="_id")
    event_name:str
    even_description:str
    start_date:datetime
    end_date:datetime
    venue_id:str
    organize_id:str
    total_tickets:int
    event_status:str
    event_type:str
    @validator('event_status')
    def status_check(cls,event_status):
        status=["upcoming, ongoing, completed, canceled"]
        if event_status not in status:
             raise ValueError(f'event_status must be in {status}')
        return event_status
    @validator("event_type")
    def type_check(cls,event_type):
        types=["concert", "conference", "webinar"]
        if event_type not in types:
             raise ValueError(f'event_type must be in {types}')
        return event_type
class UpdateEvent(BaseModel):
    event_name: Optional[str] = None
    event_description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    venue_id: Optional[str] = None
    organize_id: Optional[str] = None
    total_tickets: Optional[int] = None
    event_status: Optional[str] = None
    event_type: Optional[str] = None

    @validator('event_status', always=True)
    def status_check(cls, event_status):
        if event_status is not None:
            status = ["upcoming", "ongoing", "completed", "canceled"]
            if event_status not in status:
                raise ValueError(f'event_status must be one of {status}')
        return event_status

    @validator('event_type', always=True)
    def type_check(cls, event_type):
        if event_type is not None:
            types = ["concert", "conference", "webinar"]
            if event_type not in types:
                raise ValueError(f'event_type must be one of {types}')
        return event_type

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }
