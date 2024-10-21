from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.organizer import Organizer

# Get Organizers Collection
def get_collection_organizers(request: Request):
    return request.app.database["organizers"]

# Create an Organizer
def create_organizer(request: Request, organizer: Organizer = Body(...)):
    organizer = jsonable_encoder(organizer)
    new_organizer = get_collection_organizers(request).insert_one(organizer)
    created_organizer = get_collection_organizers(request).find_one({"_id": new_organizer.inserted_id})
    return created_organizer

# List all Organizers
def list_organizers(request: Request, limit: int):
    organizers = list(get_collection_organizers(request).find(limit=limit))
    return organizers

# Find Organizer by ID
def find_organizer(request: Request, id: str):
    if (organizer := get_collection_organizers(request).find_one({"_id": ObjectId(id)})):
        return organizer
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organizer with id {id} not found!")

# Delete Organizer by ID
def delete_organizer(request: Request, id: str):
    deleted_organizer = get_collection_organizers(request).delete_one({"_id": ObjectId(id)})

    if deleted_organizer.deleted_count == 1:
        return f"Organizer with id {id} deleted successfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organizer with id {id} not found!")
