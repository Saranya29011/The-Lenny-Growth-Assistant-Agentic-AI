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
@router.delete("/sessions/{session_id}")
def delete_session(session_id: str):

    supabase.table(
        "messages"
    ).delete().eq(
        "session_id",
        session_id
    ).execute()

    supabase.table(
        "sessions"
    ).delete().eq(
        "id",
        session_id
    ).execute()

    return {
        "message":
        "Session deleted"
    }