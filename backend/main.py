from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

from supabase import create_client

from routers.sessions import router as session_router
from routers.messages import router as message_router

from rag.retriever import retrieve_context
from services.llm import generate_response


SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

app = FastAPI(
    title="Lenny Growth Assistant"
)

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
        "message":
        "Lenny Growth Assistant Backend Running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    print(
        "Request received:",
        request
    )

    # Save User Message

    supabase.table(
        "messages"
    ).insert({
        "session_id":
        request.session_id,

        "role":
        "user",

        "content":
        request.message

    }).execute()

    # Auto Rename Session

    session = (
        supabase.table("sessions")
        .select("*")
        .eq(
            "id",
            request.session_id
        )
        .single()
        .execute()
    )

    if session.data["title"] == "New Chat":

        supabase.table(
            "sessions"
        ).update({
            "title":
            request.message[:50]
        }).eq(
            "id",
            request.session_id
        ).execute()

    # Load Chat History

    history = (
        supabase.table("messages")
        .select("*")
        .eq(
            "session_id",
            request.session_id
        )
        .order(
            "created_at"
        )
        .execute()
    )

    conversation_history = ""

    for msg in history.data[-10:]:

        conversation_history += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    # Search Query

    search_query = request.message

    followup_words = [
        "short",
        "shorter",
        "simple",
        "simpler",
        "summary",
        "summarize",
        "examples",
        "bullet points",
        "elaborate",
        "more details"
    ]

    if any(
        word in request.message.lower()
        for word in followup_words
    ):

        last_user_message = ""

        for msg in reversed(history.data):

            if (
                msg["role"] == "user"
                and msg["content"] != request.message
            ):
                last_user_message = msg["content"]
                break

        if last_user_message:

            search_query = (
                last_user_message
                + "\n" +
                request.message
            )

    # Retrieve Context

    context = retrieve_context(
        search_query
    )

    # Detect Modes

    is_ship30 = any(
        keyword in request.message.lower()
        for keyword in [
            "ship30",
            "essay",
            "article",
            "blog",
            "newsletter",
            "thread",
            "linkedin post"
        ]
    )

    is_artifact = any(
        keyword in request.message.lower()
        for keyword in [
            "html",
            "website",
            "landing page",
            "dashboard",
            "component",
            "artifact"
        ]
    )

    # Build Prompt

    if is_artifact:

        prompt = f"""
You are an expert frontend developer.

Use ONLY the transcript context below.

Generate the requested artifact.

Rules:

- Return ONLY HTML code
- Include CSS inside style tags
- Do NOT explain anything
- Do NOT use markdown
- Do NOT use ```html

Transcript Context:
{context}

Request:
{request.message}
"""

    elif is_ship30:

        prompt = f"""
You are an expert Ship30for30 writer.

Use ONLY the transcript context below.

Write a Ship30for30 style essay.

Requirements:

- Strong title
- Strong hook
- 1000 to 1250 words
- Markdown formatting
- Bold important ideas
- Bullet points
- Highly skimmable
- Examples from transcripts
- Clear takeaway section

Transcript Context:
{context}

Topic:
{request.message}
"""

    else:

        prompt = f"""
You are the Lenny Growth Assistant.

Answer ONLY using the transcript context.

IMPORTANT:

- Follow follow-up instructions such as:
  - explain simply
  - make it short
  - summarize
  - give examples
  - elaborate more

- Use previous conversation when needed.
- Do not invent information.

If information is not found in the transcript context, say:

I could not find this information in Lenny's transcripts.

Previous Conversation:
{conversation_history}

Transcript Context:
{context}

Current Question:
{request.message}
"""

    print("Generating Response...")

    ai_reply = generate_response(
        prompt
    )

    # Save Assistant Message

    if is_artifact:

        supabase.table(
            "messages"
        ).insert({
            "session_id":
            request.session_id,

            "role":
            "assistant",

            "content":
            "🚀 Artifact generated → Open the viewer panel"

        }).execute()

    else:

        supabase.table(
            "messages"
        ).insert({
            "session_id":
            request.session_id,

            "role":
            "assistant",

            "content":
            ai_reply

        }).execute()

    return {
        "response": ai_reply,
        "artifact": is_artifact
    }