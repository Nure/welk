from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/")
async def read_items():
    return {"message": "Fetching all items", "status": "success"}

@router.get("/error")
async def trigger_error():
    # This will log an INFO level but simulate a logic error
    return {"message": "Simulated error", "status": "failed"}