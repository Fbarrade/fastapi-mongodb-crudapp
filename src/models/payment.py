from pydantic import BaseModel, Field,  validator
from datetime import datetime
import uuid
from typing import Optional

class Payment(BaseModel):
    payment_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    attendee_id: str  # Foreign key to Attendees collection
    amount: float
    payment_date: datetime
    payment_method: str
    payment_status: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
        }

class UpdatePayment(BaseModel):
    attendee_id: Optional[str] = None
    amount: Optional[float] = None
    payment_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None

    @validator('amount')
    def amount_check(cls, amount):
        if amount is not None and amount < 0:
            raise ValueError('Amount must be non-negative.')
        return amount

    class Config:
        allow_population_by_field_name = True
