from pathlib import Path

documents = []

folder = Path("../lennys-podcast-transcripts/episodes")

print("Folder Exists:", folder.exists())
print("Absolute Path:", folder.resolve())

for file in folder.rglob("transcript.md"):

    print(file)

    with open(file, "r", encoding="utf-8") as f:

        text = f.read()

        documents.append(
            {
                "file": str(file),
                "content": text
            }
        )

print("Total transcripts:", len(documents))