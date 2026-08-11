from langchain_ollama import OllamaEmbeddings


def get_embedding_model() -> OllamaEmbeddings:
    return OllamaEmbeddings(
        model="nomic-embed-text",
    )