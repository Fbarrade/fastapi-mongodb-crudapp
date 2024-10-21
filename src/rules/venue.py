from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.venue import Venue

# Get Venues Collection
def get_collection_venues(request: Request):
    return request.app.database["venues"]

# Create a Venue
def create_venue(request: Request, venue: Venue = Body(...)):
    venue = jsonable_encoder(venue)
    new_venue = get_collection_venues(request).insert_one(venue)
    created_venue = get_collection_venues(request).find_one({"_id": new_venue.inserted_id})
    return created_venue

# List all Venues
def list_venues(request: Request, limit: int):
    venues = list(get_collection_venues(request).find(limit=limit))
    return venues

# Find Venue by ID
def find_venue(request: Request, id: str):
    if (venue := get_collection_venues(request).find_one({"_id": ObjectId(id)})):
        return venue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Venue with id {id} not found!")

# Delete Venue by ID
def delete_venue(request: Request, id: str):
    deleted_venue = get_collection_venues(request).delete_one({"_id": ObjectId(id)})

    if deleted_venue.deleted_count == 1:
        return f"Venue with id {id} deleted successfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Venue with id {id} not found!")
