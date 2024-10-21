from fastapi import APIRouter
from src.endpoints import event, organizer, venue, ticket, attendee, payment # Import all endpoint modules

router = APIRouter()
router.include_router(event.router)
router.include_router(organizer.router)  # Include organizers router
router.include_router(venue.router)      # Include venues router
router.include_router(ticket.router)     # Include tickets router
router.include_router(attendee.router)   # Include attendees router
router.include_router(payment.router)    # Include payments router

