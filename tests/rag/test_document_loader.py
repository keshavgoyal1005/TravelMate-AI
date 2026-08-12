from app.rag.document_loader import load_travel_documents


def test_load_travel_documents():
    documents = load_travel_documents()

    assert len(documents) >= 5


def test_documents_have_content():
    documents = load_travel_documents()

    for document in documents:
        assert document.page_content.strip()


def test_documents_have_metadata():
    documents = load_travel_documents()

    for document in documents:
        assert "source" in document.metadata