# UI / UX Design Document

## Design Philosophy

The design focuses on simplicity, familiarity, and productivity.

The goal is to create an experience similar to ChatGPT and Claude while supporting artifact generation.

---

# Design Goals

## Simplicity

Users should be able to start chatting immediately.

## Familiarity

The interface follows patterns users already know from modern AI products.

## Efficiency

Actions such as creating sessions and viewing artifacts require minimal effort.

---

# Layout Structure

```text
----------------------------------------------------
| Sidebar | Chat Window | Artifact Viewer          |
----------------------------------------------------
```

---

# Sidebar

Purpose:

- Session navigation
- Session creation
- Session deletion

Features:

- New Chat button
- Session history
- Active session highlighting

---

# Chat Window

Purpose:

Display conversation history.

Features:

- User messages
- Assistant messages
- Auto scroll
- Loading indicator

---

# Artifact Viewer

Purpose:

Display generated HTML artifacts separately from chat.

Features:

- Responsive iframe rendering
- Side-by-side viewing
- Dynamic resizing

---

# Color Palette

| Element | Color |
|----------|----------|
| Primary | #2563eb |
| Background | #f9fafb |
| Border | #e5e7eb |
| Text | #111827 |
| Secondary Text | #6b7280 |

---

# Typography

Primary Font:

```text
System UI
Segoe UI
Roboto
Sans-serif
```

Goals:

- High readability
- Clean appearance
- Consistent spacing

---

# UX Decisions

## Session Persistence

Chats remain available across page refreshes.

## Auto Session Naming

First user message becomes session title.

## Artifact Isolation

Generated HTML appears in a dedicated viewer rather than cluttering the conversation.

## Auto Scrolling

Newest messages automatically remain visible.

---

# Responsiveness

Desktop:

```text
Sidebar + Chat + Artifact
```

Mobile:

```text
Sidebar
Chat
Artifact
```

Stacked vertically.

---

# Future Design Enhancements

- Dark Mode
- Markdown Rendering
- Streaming Messages
- Multi-Panel Layouts
- Resizable Artifact Viewer
