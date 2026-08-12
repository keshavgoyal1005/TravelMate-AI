from app.rag.retriever import get_travel_retriever


def test_retriever_returns_documents():
    retriever = get_travel_retriever()

    results = retriever.invoke(
        "What transportation is available in Paris?"
    )

    assert results
    assert len(results) <= 3


def test_retriever_returns_document_objects():
    retriever = get_travel_retriever()

    results = retriever.invoke(
        "What are the famous attractions in Paris?"
    )

    assert results

    for document in results:
        assert document.page_content
        assert "source" in document.metadata