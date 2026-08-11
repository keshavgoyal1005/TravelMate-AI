from app.rag.document_loader import load_travel_documents
from app.rag.document_splitter import split_documents
from app.rag.vector_store import create_vector_store


def ingest_travel_knowledge():
    documents = load_travel_documents()

    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    return vector_store