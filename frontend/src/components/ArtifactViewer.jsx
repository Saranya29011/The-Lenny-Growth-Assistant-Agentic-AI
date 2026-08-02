function ArtifactViewer({
  artifact
}) {

  return (

    <div
      style={{
        width: "100%",
        height: "100%",
        background: "#fafafa"
      }}
    >

      <div
        style={{
          padding: "12px",
          borderBottom:
            "1px solid #ddd",
          fontWeight: "bold"
        }}
      >
        Artifact Viewer
      </div>

      {!artifact ? (

        <div
          style={{
            padding: "30px",
            color: "#6b7280"
          }}
        >
          Generate HTML/CSS artifacts
          to preview them here.
        </div>

      ) : (

        <iframe
          title="artifact"
          srcDoc={artifact}
          style={{
            width: "100%",
            height: "95%",
            border: "none",
            background: "white"
          }}
        />

      )}

    </div>

  );
}

export default ArtifactViewer;