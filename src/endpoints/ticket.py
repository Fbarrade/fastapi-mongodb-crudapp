from fastapi import APIRouter, Request, status
from typing import List
from src.models.ticket import Ticket, UpdateTicket
import src.rules.ticket as tickets

router = APIRouter(prefix="/tickets", tags=["Tickets"])

@router.post("/", response_description="Create a ticket", status_code=status.HTTP_201_CREATED, response_model=Ticket)
def create_ticket(request: Request, ticket: Ticket):
    return tickets.create_ticket(request, ticket)

@router.put("/{id}", response_description="Update a ticket", response_model=Ticket)
def update_ticket(request: Request, id: str, ticket: UpdateTicket):
    return tickets.update_ticket(request, id, ticket)

@router.get("/", response_description="List all tickets", response_model=List[Ticket])
def list_tickets(request: Request):
    return tickets.list_tickets(request, 100)

@router.get("/{id}/", response_description="Get ticket by id", response_model=Ticket)
def find_ticket_by_id(request: Request, id: str):
    return tickets.find_ticket(request, id)

@router.delete("/{id}", response_description="Delete a ticket")
def delete_ticket(request: Request, id: str):
    return tickets.delete_ticket(request, id)
