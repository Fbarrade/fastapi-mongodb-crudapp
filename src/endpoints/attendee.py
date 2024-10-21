from fastapi import APIRouter, Request, status
from typing import List
from src.models.attendee import Attendee, UpdateAttendee
import src.rules.attendee as attendees

router = APIRouter(prefix="/attendees", tags=["Attendees"])

@router.post("/", response_description="Create an attendee", status_code=status.HTTP_201_CREATED, response_model=Attendee)
def create_attendee(request: Request, attendee: Attendee):
    return attendees.create_attendee(request, attendee)

@router.put("/{id}", response_description="Update an attendee", response_model=Attendee)
def update_attendee(request: Request, id: str, attendee: UpdateAttendee):
    return attendees.update_attendee(request, id, attendee)

@router.get("/", response_description="List all attendees", response_model=List[Attendee])
def list_attendees(request: Request):
    return attendees.list_attendees(request, 100)

@router.get("/{id}/", response_description="Get attendee by id", response_model=Attendee)
def find_attendee_by_id(request: Request, id: str):
    return attendees.find_attendee(request, id)

@router.delete("/{id}", response_description="Delete an attendee")
def delete_attendee(request: Request, id: str):
    return attendees.delete_attendee(request, id)
