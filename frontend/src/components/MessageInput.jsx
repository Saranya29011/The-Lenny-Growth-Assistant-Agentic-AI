function MessageInput({
  message,
  setMessage,
  sendMessage,
  loading
}) {
  return (
    <div
      style={{
        display: "flex",
        padding: "15px",
        borderTop: "1px solid #ddd",
        gap: "10px"
      }}
    >
      <input
        style={{
          flex: 1,
          padding: "12px"
        }}
        value={message}
        onChange={(e) =>
          setMessage(e.target.value)
        }
        placeholder="Ask Lenny..."
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />

      <button
        onClick={sendMessage}
        disabled={loading}
      >
        {loading ? "..." : "Send"}
      </button>
    </div>
  );
}

export default MessageInput;