from fastapi import APIRouter
from database import supabase

router = APIRouter()


@router.get("/messages/{session_id}")
def get_messages(session_id: str):

    result = (
        supabase.table("messages")
        .select("*")
        .eq("session_id", session_id)
        .order("created_at")
        .execute()
    )

    return result.data