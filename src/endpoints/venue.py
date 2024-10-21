from fastapi import APIRouter, Request, status
from typing import List
from src.models.venue import Venue, UpdateVenue
import src.rules.venue as venues

router = APIRouter(prefix="/venues", tags=["Venues"])

@router.post("/", response_description="Create a venue", status_code=status.HTTP_201_CREATED, response_model=Venue)
def create_venue(request: Request, venue: Venue):
    return venues.create_venue(request, venue)

@router.put("/{id}", response_description="Update a venue", response_model=Venue)
def update_venue(request: Request, id: str, venue: UpdateVenue):
    return venues.update_venue(request, id, venue)

@router.get("/", response_description="List all venues", response_model=List[Venue])
def list_venues(request: Request):
    return venues.list_venues(request, 100)

@router.get("/{id}/", response_description="Get venue by id", response_model=Venue)
def find_venue_by_id(request: Request, id: str):
    return venues.find_venue(request, id)

@router.delete("/{id}", response_description="Delete a venue")
def delete_venue(request: Request, id: str):
    return venues.delete_venue(request, id)
