from fastapi import APIRouter, Request, status
from typing import List
from src.models.organizer import Organizer, UpdateOrganizer
import src.rules.organizer as organizers

router = APIRouter(prefix="/organizers", tags=["Organizers"])

@router.post("/", response_description="Create an organizer", status_code=status.HTTP_201_CREATED, response_model=Organizer)
def create_organizer(request: Request, organizer: Organizer):
    return organizers.create_organizer(request, organizer)

@router.put("/{id}", response_description="Update an organizer", response_model=Organizer)
def update_organizer(request: Request, id: str, organizer: UpdateOrganizer):
    return organizers.update_organizer(request, id, organizer)

@router.get("/", response_description="List all organizers", response_model=List[Organizer])
def list_organizers(request: Request):
    return organizers.list_organizers(request, 100)

@router.get("/{id}/", response_description="Get organizer by id", response_model=Organizer)
def find_organizer_by_id(request: Request, id: str):
    return organizers.find_organizer(request, id)

@router.delete("/{id}", response_description="Delete an organizer")
def delete_organizer(request: Request, id: str):
    return organizers.delete_organizer(request, id)
