from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.attendee import Attendee

# Get Attendees Collection
def get_collection_attendees(request: Request):
    return request.app.database["attendees"]

# Create an Attendee
def create_attendee(request: Request, attendee: Attendee = Body(...)):
    attendee = jsonable_encoder(attendee)
    new_attendee = get_collection_attendees(request).insert_one(attendee)
    created_attendee = get_collection_attendees(request).find_one({"_id": new_attendee.inserted_id})
    return created_attendee

# List all Attendees
def list_attendees(request: Request, limit: int):
    attendees = list(get_collection_attendees(request).find(limit=limit))
    return attendees

# Find Attendee by ID
def find_attendee(request: Request, id: str):
    if (attendee := get_collection_attendees(request).find_one({"_id": ObjectId(id)})):
        return attendee
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Attendee with id {id} not found!")

# Delete Attendee by ID
def delete_attendee(request: Request, id: str):
    deleted_attendee = get_collection_attendees(request).delete_one({"_id": ObjectId(id)})

    if deleted_attendee.deleted_count == 1:
        return f"Attendee with id {id} deleted successfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Attendee with id {id} not found!")
