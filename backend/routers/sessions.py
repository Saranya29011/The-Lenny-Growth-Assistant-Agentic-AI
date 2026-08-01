from fastapi import APIRouter
from database import supabase

router = APIRouter()

@router.post("/sessions")
def create_session():

    result = supabase.table("sessions").insert(
        {
            "title": "New Chat"
        }
    ).execute()

    return result.data


@router.get("/sessions")
def get_sessions():

    result = (
        supabase.table("sessions")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return result.data