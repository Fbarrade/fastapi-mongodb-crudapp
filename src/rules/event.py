from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.event import Event, UpdateEvent

def get_collection_events(request: Request):
    return request.app.database["events"]

def create_event(request: Request, event: Event = Body(...)):
    event = jsonable_encoder(event)
    new_event = get_collection_events(request).insert_one(event)
    created_event = get_collection_events(request).find_one({"_id": new_event.inserted_id})
    return created_event

def list_events(request: Request, limit: int):
    events = list(get_collection_events(request).find(limit=limit))
    return events

def find_event(request: Request, id: str):
    if (event := get_collection_events(request).find_one({"_id": ObjectId(id)})):
        return event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} not found!")

def update_event(request: Request, id: str, event: UpdateEvent):
    existing_event = get_collection_events(request).find_one({"_id": ObjectId(id)})
    if existing_event:
        update_data = {k: v for k, v in event.dict().items() if v is not None}
        get_collection_events(request).update_one({"_id": ObjectId(id)}, {"$set": update_data})
        updated_event = get_collection_events(request).find_one({"_id": ObjectId(id)})
        return updated_event
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} not found!")

def delete_event(request: Request, id: str):
    deleted_event = get_collection_events(request).delete_one({"_id": ObjectId(id)})
    if deleted_event.deleted_count == 1:
        return f"Event with id {id} deleted successfully"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with id {id} not found!")
