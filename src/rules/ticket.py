from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.ticket import Ticket

# Get Tickets Collection
def get_collection_tickets(request: Request):
    return request.app.database["tickets"]

# Create a Ticket
def create_ticket(request: Request, ticket: Ticket = Body(...)):
    ticket = jsonable_encoder(ticket)
    new_ticket = get_collection_tickets(request).insert_one(ticket)
    created_ticket = get_collection_tickets(request).find_one({"_id": new_ticket.inserted_id})
    return created_ticket

# List all Tickets
def list_tickets(request: Request, limit: int):
    tickets = list(get_collection_tickets(request).find(limit=limit))
    return tickets

# Find Ticket by ID
def find_ticket(request: Request, id: str):
    if (ticket := get_collection_tickets(request).find_one({"_id": ObjectId(id)})):
        return ticket
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket with id {id} not found!")

# Delete Ticket by ID
def delete_ticket(request: Request, id: str):
    deleted_ticket = get_collection_tickets(request).delete_one({"_id": ObjectId(id)})

    if deleted_ticket.deleted_count == 1:
        return f"Ticket with id {id} deleted successfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Ticket with id {id} not found!")
