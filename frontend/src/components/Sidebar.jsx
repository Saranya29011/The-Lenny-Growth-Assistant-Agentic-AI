function Sidebar({
  sessions,
  currentSession,
  setCurrentSession,
  createSession,
  deleteSession
}) {

  return (
    <div
      style={{
        width: "280px",
        background: "#111827",
        color: "white",
        display: "flex",
        flexDirection: "column",
        padding: "15px",
        height: "100vh"
      }}
    >

      <button
        onClick={createSession}
        style={{
          padding: "12px",
          borderRadius: "10px",
          border: "none",
          background: "#2563eb",
          color: "white",
          fontWeight: "bold",
          cursor: "pointer",
          marginBottom: "20px"
        }}
      >
        + New Chat
      </button>

      <div
        style={{
          overflowY: "auto",
          flex: 1
        }}
      >
        {sessions.map((session) => (

          <div
            key={session.id}
            onClick={() =>
              setCurrentSession(
                session.id
              )
            }
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              padding: "12px",
              borderRadius: "10px",
              marginBottom: "8px",
              cursor: "pointer",
              background:
                currentSession === session.id
                  ? "#1f2937"
                  : "transparent"
            }}
          >

            <span
              style={{
                fontSize: "14px",
                flex: 1,
                overflow: "hidden",
                whiteSpace: "nowrap",
                textOverflow: "ellipsis"
              }}
            >
              {session.title}
            </span>

            <button
              onClick={(e) => {
                e.stopPropagation();
                deleteSession(session.id);
              }}
              style={{
                border: "none",
                background: "transparent",
                cursor: "pointer",
                color: "#9ca3af"
              }}
            >
              🗑
            </button>

          </div>

        ))}
      </div>

    </div>
  );
}

export default Sidebar;