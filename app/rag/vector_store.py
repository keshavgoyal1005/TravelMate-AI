from langchain_chroma import Chroma
from langchain_core.documents import Document
from app.rag.embeddings import get_embedding_model


COLLECTION_NAME = "travelmate_travel"
PERSIST_DIRECTORY = "chroma_db"


def create_vector_store(
    documents: list[Document],
) -> Chroma:
    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
    )

    return vector_store