import { useEffect, useRef } from "react";

function ChatWindow({ messages }) {

  const bottomRef = useRef(null);

  useEffect(() => {

    bottomRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages]);

  return (

    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "15px"
      }}
    >

      {messages.map((msg) => {

        const isHtml =
          msg.content?.includes("<html") ||
          msg.content?.includes("<body") ||
          msg.content?.includes("<style") ||
          msg.content?.includes("<!DOCTYPE");

        return (

          <div
            key={msg.id}
            style={{
              display: "flex",
              justifyContent:
                msg.role === "user"
                  ? "flex-end"
                  : "flex-start"
            }}
          >

            <div
              style={{
                maxWidth: "75%",
                padding: "14px 18px",
                borderRadius: "16px",
                lineHeight: "1.7",
                fontSize: "15px",
                whiteSpace: "pre-wrap",
                wordBreak: "break-word",
                boxShadow:
                  "0 2px 8px rgba(0,0,0,0.08)",
                background:
                  msg.role === "user"
                    ? "#2563eb"
                    : "#ffffff",
                color:
                  msg.role === "user"
                    ? "#ffffff"
                    : "#111827",
                border:
                  msg.role === "assistant"
                    ? "1px solid #e5e7eb"
                    : "none"
              }}
            >

              {isHtml ? (

                <div>
                  🚀 Artifact generated
                  <br />
                  Open the viewer panel on
                  the right side.
                </div>

              ) : (

                msg.content

              )}

            </div>

          </div>

        );

      })}

      <div ref={bottomRef} />

    </div>

  );

}

export default ChatWindow;