# Architecture Document

## System Architecture

```text
                    +--------------------+
                    |   React Frontend   |
                    +--------------------+
                              |
                              |
                              v
                    +--------------------+
                    |   FastAPI Backend  |
                    +--------------------+
                              |
        -----------------------------------------
        |                    |                  |
        v                    v                  v
+---------------+   +---------------+   +---------------+
| Sessions API  |   | Messages API  |   |  Chat API     |
+---------------+   +---------------+   +---------------+
                                              |
                                              v
                                    +------------------+
                                    | RAG Retriever    |
                                    +------------------+
                                              |
                                              v
                                    +------------------+
                                    | Transcript Data  |
                                    +------------------+
                                              |
                                              v
                                    +------------------+
                                    | Gemini / Ollama  |
                                    +------------------+
                                              |
                                              v
                                    +------------------+
                                    |    Supabase      |
                                    +------------------+
```

---

# Database Schema

## sessions

| Column | Type |
|----------|----------|
| id | UUID |
| title | TEXT |
| created_at | TIMESTAMP |

---

## messages

| Column | Type |
|----------|----------|
| id | UUID |
| session_id | UUID |
| role | TEXT |
| content | TEXT |
| created_at | TIMESTAMP |

---

# API Endpoints

## Session APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /sessions | Get all sessions |
| POST | /sessions | Create new session |
| DELETE | /sessions/{id} | Delete session |

---

## Message APIs

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /messages/{session_id} | Get chat history |

---

## Chat API

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /chat | Main AI endpoint |

---

# Agentic Routing Logic

The application routes requests based on user intent.

```text
User Query
     |
     v
Intent Detection
     |
----------------------------------
|              |                |
Normal Chat   Ship30 Mode   Artifact Mode
```

---

## Normal Chat Flow

```text
User Question
      |
      v
Retrieve Context
      |
      v
Prompt Creation
      |
      v
Gemini / Ollama
      |
      v
Response
```

---

## Ship30 Essay Flow

```text
Essay Request
      |
      v
Transcript Retrieval
      |
      v
Essay Prompt
      |
      v
LLM
      |
      v
Long-form Essay
```

---

## Artifact Flow

```text
HTML Request
      |
      v
Retrieve Context
      |
      v
Frontend Prompt
      |
      v
LLM
      |
      v
HTML Artifact
      |
      v
Artifact Viewer
```

---

# LLM Toggle System

The application supports multiple LLM providers.

Configuration:

```env
LLM_PROVIDER=gemini
```

or

```env
LLM_PROVIDER=ollama
```

Routing Logic:

```text
Incoming Request
       |
       v
Check LLM_PROVIDER
       |
 --------------------
 |                  |
Gemini          Ollama
 |                  |
 v                  v
Response        Response
```

---

# Artifact Viewer Architecture

```text
Generated HTML
       |
       v
Backend Response
       |
       v
React State
       |
       v
ArtifactViewer Component
       |
       v
iframe srcDoc
       |
       v
Rendered Artifact
```

---

# Security Considerations

- API keys stored in environment variables
- No secrets committed to repository
- Supabase handles secure database access
- CORS enabled for frontend communication

---

