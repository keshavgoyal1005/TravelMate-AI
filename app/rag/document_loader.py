from pathlib import Path

from langchain_core.documents import Document


KNOWLEDGE_DIR = Path("travel_knowledge")


def load_travel_documents() -> list[Document]:
    documents: list[Document] = []

    for file_path in KNOWLEDGE_DIR.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        document = Document(
            page_content=content,
            metadata={
                "source": str(file_path),
            },
        )

        documents.append(document)

    return documents