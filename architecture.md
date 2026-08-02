# Architecture Document

## Lenny Growth Assistant

---

# System Overview

Lenny Growth Assistant is a Retrieval-Augmented Generation (RAG) application designed to help users interact with Lenny Rachitsky's podcast transcripts through an AI-powered chat interface.

The system retrieves relevant transcript context from a knowledge base and combines it with a Large Language Model (LLM) to generate accurate and contextual responses.

---

# High-Level Architecture

```text
+------------------+
|   React Frontend |
+---------+--------+
          |
          | REST API
          v
+------------------+
| FastAPI Backend  |
+---------+--------+
          |
          |
          +----------------+
          |                |
          v                v
+----------------+   +----------------+
| RAG Retriever  |   |    Supabase    |
| (Embeddings)   |   | Sessions & Msg |
+--------+-------+   +----------------+
         |
         v
+----------------+
| Transcript DB  |
| / Vector Store |
+--------+-------+
         |
         v
+----------------+
| Gemini/Ollama  |
|      LLM       |
+----------------+
```

---

# Architecture Layers

## 1. Presentation Layer

### Technology
- React
- Vite
- Axios

### Responsibilities

- User Interface
- Chat Experience
- Session Navigation
- Artifact Viewer
- Message Input Handling

### Components

- App.jsx
- Sidebar.jsx
- ChatWindow.jsx
- MessageInput.jsx
- ArtifactViewer.jsx

---

## 2. API Layer

### Technology
- FastAPI

### Responsibilities

- Handle User Requests
- Manage Sessions
- Store Messages
- Retrieve Context
- Communicate with LLM

### Main Endpoints

| Endpoint | Method | Purpose |
|-----------|----------|----------|
| / | GET | Health Check |
| /chat | POST | Generate Response |
| /sessions | GET | Fetch Sessions |
| /sessions | POST | Create Session |
| /sessions/{id} | DELETE | Delete Session |
| /messages/{id} | GET | Load Messages |

---

## 3. Retrieval Layer (RAG)

### Responsibilities

- Convert Query to Embeddings
- Search Relevant Transcript Chunks
- Retrieve Context for LLM

### Modules

```text
rag/
├── embedder.py
├── retriever.py
└── ingest.py
```

### Workflow

1. User sends question
2. Query converted into embeddings
3. Similar transcript chunks retrieved
4. Context sent to LLM

---

## 4. LLM Layer

### Supported Models

#### Gemini

- Gemini 2.5 Flash
- Cloud-based inference

#### Ollama

- Qwen
- Llama
- Mistral
- Local inference

### Responsibilities

- Answer Questions
- Generate Summaries
- Create Ship30 Essays
- Generate HTML Artifacts

---

## 5. Database Layer

### Technology

Supabase

### Tables

#### sessions

| Field | Type |
|---------|--------|
| id | UUID |
| title | TEXT |
| created_at | TIMESTAMP |

#### messages

| Field | Type |
|---------|--------|
| id | UUID |
| session_id | UUID |
| role | TEXT |
| content | TEXT |
| created_at | TIMESTAMP |

### Responsibilities

- Store Chat Sessions
- Store Messages
- Maintain Conversation History

---

# Request Flow

## Normal Question Answering

```text
User Question
      |
      v
React Frontend
      |
      v
FastAPI Backend
      |
      v
RAG Retriever
      |
      v
Transcript Context
      |
      v
Gemini / Ollama
      |
      v
Generated Response
      |
      v
Supabase Storage
      |
      v
Frontend Display
```

---

## Artifact Generation Flow

```text
User Request
(Create Dashboard / Website)
          |
          v
FastAPI Backend
          |
          v
Prompt Builder
          |
          v
Gemini / Ollama
          |
          v
HTML Artifact
          |
          v
Artifact Viewer
```

---

# Folder Structure

```text
project-root/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── rag/
│   ├── routers/
│   ├── services/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   └── package.json
│
├── README.md
├── architecture.md
├── design.md
└── PRD.md
```

---

# Key Features

- Retrieval-Augmented Generation (RAG)
- Multi-Session Chat
- Context-Aware Conversations
- Ship30 Content Generation
- HTML Artifact Generation
- Gemini Integration
- Ollama Integration
- Supabase Persistence

---

