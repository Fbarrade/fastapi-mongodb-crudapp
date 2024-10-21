from pydantic import BaseModel, Field, validator
import uuid
from typing import Optional
class Venue(BaseModel):
    venue_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    venue_name: str
    address: str
    city: str
    state: str
    capacity: int
    venue_description: Optional[str] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class UpdateVenue(BaseModel):
    venue_name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    capacity: Optional[int] = None
    venue_description: Optional[str] = None

    @validator('capacity')
    def capacity_check(cls, capacity):
        if capacity is not None and capacity < 1:
            raise ValueError('Capacity must be at least 1.')
        return capacity

    class Config:
        allow_population_by_field_name = True
