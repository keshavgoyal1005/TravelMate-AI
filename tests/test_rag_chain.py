from langchain_core.documents import Document

from app.rag.chain import format_documents


def test_format_documents():
    documents = [
        Document(
            page_content="Paris has the Eiffel Tower.",
            metadata={"source": "paris.txt"},
        ),
        Document(
            page_content="Paris has the Louvre Museum.",
            metadata={"source": "paris.txt"},
        ),
    ]

    context = format_documents(documents)

    assert "Eiffel Tower" in context
    assert "Louvre Museum" in context