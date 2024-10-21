from fastapi import APIRouter, Request, status
from typing import List
from src.models.event import Event, UpdateEvent
import src.rules.event as events

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/", response_description="Create an event", status_code=status.HTTP_201_CREATED, response_model=Event)
def create_event(request: Request, event: Event):
    return events.create_event(request, event)

@router.put("/{id}", response_description="Update an event", response_model=Event)
def update_event(request: Request, id: str, event: UpdateEvent):
    return events.update_event(request, id, event)

@router.get("/", response_description="List all events", response_model=List[Event])
def list_events(request: Request):
    return events.list_events(request, 100)

@router.get("/{id}/", response_description="Get event by id", response_model=Event)
def find_event_by_id(request: Request, id: str):
    return events.find_event(request, id)

@router.delete("/{id}", response_description="Delete an event")
def delete_event(request: Request, id: str):
    return events.delete_event(request, id)
