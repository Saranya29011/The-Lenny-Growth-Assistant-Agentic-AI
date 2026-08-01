from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import ollama
from supabase import create_client
from routers.sessions import router as session_router
from routers.messages import router as message_router
from rag.retriever import retrieve_context

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="Lenny Growth Assistant")
app.include_router(session_router)
app.include_router(message_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/")
def home():
    return {
        "message": "Lenny Growth Assistant Backend Running"
    }

@app.post("/chat")
def chat(request: ChatRequest):

    print("Request received:", request)

    # Save user message
    result = supabase.table("messages").insert({
        "session_id": request.session_id,
        "role": "user",
        "content": request.message
    }).execute()

    context = retrieve_context(request.message)

    prompt = f"""
    You are the Lenny Growth Assistant.

    Answer ONLY using the transcript context below.

    If the answer is not found in the transcripts, say:
    'I could not find this information in Lenny's transcripts.'

    Transcript Context:
    {context}

    Question:
    {request.message}
    """

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    ai_reply = response["message"]["content"]

    result = supabase.table("messages").insert({
        "session_id": request.session_id,
        "role": "assistant",
        "content": ai_reply
    }).execute()

    return {
        "response": ai_reply
    }