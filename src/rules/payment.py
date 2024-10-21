from fastapi import Body, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.payment import Payment

# Get Payments Collection
def get_collection_payments(request: Request):
    return request.app.database["payments"]

# Create a Payment
def create_payment(request: Request, payment: Payment = Body(...)):
    payment = jsonable_encoder(payment)
    new_payment = get_collection_payments(request).insert_one(payment)
    created_payment = get_collection_payments(request).find_one({"_id": new_payment.inserted_id})
    return created_payment

# List all Payments
def list_payments(request: Request, limit: int):
    payments = list(get_collection_payments(request).find(limit=limit))
    return payments

# Find Payment by ID
def find_payment(request: Request, id: str):
    if (payment := get_collection_payments(request).find_one({"_id": ObjectId(id)})):
        return payment
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {id} not found!")

# Delete Payment by ID
def delete_payment(request: Request, id: str):
    deleted_payment = get_collection_payments(request).delete_one({"_id": ObjectId(id)})

    if deleted_payment.deleted_count == 1:
        return f"Payment with id {id} deleted successfully"
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Payment with id {id} not found!")
