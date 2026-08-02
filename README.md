# Lenny Growth Assistant

## Overview

Lenny Growth Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to interact with Lenny's podcast transcripts through a conversational interface.

The application supports:

- Transcript-based Q&A
- Session management
- Long-form content generation
- HTML artifact generation
- Gemini and Ollama model switching
- Persistent chat history using Supabase

---

## Features

### Chat with Lenny Transcripts
Ask questions and receive answers grounded in transcript content.

### Session Management
- Create chats
- View previous chats
- Delete chats

### RAG Pipeline
Relevant transcript chunks are retrieved before generating responses.

### Artifact Generation
Generate:
- Landing Pages
- Dashboards
- Components
- HTML Prototypes

### LLM Switching
Choose between:

- Gemini API
- Ollama Local Models

### Persistent Storage
All sessions and messages are stored in Supabase.

---

## Tech Stack

### Frontend
- React
- Vite

### Backend
- FastAPI
- Python

### Database
- Supabase

### AI Models
- Gemini 2.5 Flash
- Ollama

---

## Project Structure

```text
frontend/
backend/

backend/
├── routers/
├── services/
├── rag/
├── main.py

frontend/
├── components/
├── services/
├── App.jsx
```

---

## Architecture Overview

```text
React Frontend
      |
      v
FastAPI Backend
      |
      v
Chat Endpoint
      |
      v
Retriever
      |
      v
Transcript Chunks
      |
      v
Gemini / Ollama
      |
      v
Supabase
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

cd project
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## Environment Variables

Create a `.env` file inside backend.

```env
LLM_PROVIDER=gemini

OLLAMA_MODEL=qwen2.5:3b

GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
SUPABASE_URL=<YOUR_SUPABASE_URL>
SUPABASE_KEY=<YOUR_SUPABASE_KEY>
```

---

## API Endpoints

| Method | Endpoint | Description |
|----------|------------|-------------|
| GET | / | Health Check |
| GET | /sessions | Fetch Sessions |
| POST | /sessions | Create Session |
| DELETE | /sessions/{id} | Delete Session |
| GET | /messages/{id} | Fetch Messages |
| POST | /chat | Chat Endpoint |

---

## Screenshots

### Chat Interface

<img width="1914" height="1011" alt="{35343A40-3200-4EE6-A6E5-961EFEBBA709}" src="https://github.com/user-attachments/assets/f9395c44-b6b0-4d7c-b659-1f0cb9ead85d" />

### Artifact Viewer

<img width="1915" height="1023" alt="{0BC6FAA3-6190-4AC4-9996-91187563BC42}" src="https://github.com/user-attachments/assets/bec31654-3bf5-47d2-a1af-4e7da5cc72c3" />


