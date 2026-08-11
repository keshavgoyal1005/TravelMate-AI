from app.rag.document_loader import load_travel_documents
from app.rag.document_splitter import split_documents


def test_documents_are_split():
    documents = load_travel_documents()

    chunks = split_documents(documents)

    assert len(chunks) > len(documents)


def test_chunks_have_content():
    documents = load_travel_documents()

    chunks = split_documents(documents)

    for chunk in chunks:
        assert chunk.page_content.strip()


def test_chunks_preserve_metadata():
    documents = load_travel_documents()

    chunks = split_documents(documents)

    for chunk in chunks:
        assert "source" in chunk.metadata