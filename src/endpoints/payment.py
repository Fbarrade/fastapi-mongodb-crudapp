from fastapi import APIRouter, Request, status
from typing import List
from src.models.payment import Payment, UpdatePayment
import src.rules.payment as payments

router = APIRouter(prefix="/payments", tags=["Payments"])

@router.post("/", response_description="Create a payment", status_code=status.HTTP_201_CREATED, response_model=Payment)
def create_payment(request: Request, payment: Payment):
    return payments.create_payment(request, payment)

@router.put("/{id}", response_description="Update a payment", response_model=Payment)
def update_payment(request: Request, id: str, payment: UpdatePayment):
    return payments.update_payment(request, id, payment)

@router.get("/", response_description="List all payments", response_model=List[Payment])
def list_payments(request: Request):
    return payments.list_payments(request, 100)

@router.get("/{id}/", response_description="Get payment by id", response_model=Payment)
def find_payment_by_id(request: Request, id: str):
    return payments.find_payment(request, id)

@router.delete("/{id}", response_description="Delete a payment")
def delete_payment(request: Request, id: str):
    return payments.delete_payment(request, id)
