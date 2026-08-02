# Lenny Growth Assistant

An AI-powered Growth Assistant that helps users explore, search, and generate insights from Lenny Rachitsky's podcast transcripts.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant transcript context and generate accurate responses using Gemini or Ollama.

## Features

- AI-powered transcript search
- Multi-session chat history
- Context-aware follow-up questions
- Ship30 style content generation
- HTML artifact generation
- Supabase database integration
- Gemini and Ollama support
- React frontend
- FastAPI backend

## Tech Stack

### Frontend
- React
- Axios
- Vite

### Backend
- FastAPI
- Python
- Supabase

### AI
- Gemini 2.5 Flash
- Ollama
- Nomic Embeddings

## Project Structure

backend/
- main.py
- rag/
- services/
- routers/

frontend/
- components/
- services/
- App.jsx

## Installation

### Backend

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
## Environment Variables
LLM_PROVIDER=gemini

OLLAMA_MODEL=qwen2.5:3b

GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>

SUPABASE_URL=<YOUR_SUPABASE_URL>

SUPABASE_KEY=<YOUR_SUPABASE_KEY>
### Frontend
``` bash
npm install
npm run dev
```
