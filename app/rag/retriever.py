from langchain_chroma import Chroma

from app.rag.embeddings import get_embedding_model


COLLECTION_NAME = "travelmate_travel"
PERSIST_DIRECTORY = "chroma_db"


def get_vector_store() -> Chroma:
    embedding_model = get_embedding_model()

    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embedding_model,
    )


def get_travel_retriever():
    vector_store = get_vector_store()

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )