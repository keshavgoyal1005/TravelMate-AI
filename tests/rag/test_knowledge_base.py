from pathlib import Path


KNOWLEDGE_DIR = Path("travel_knowledge")


def test_knowledge_base_exists():
    assert KNOWLEDGE_DIR.exists()
    assert KNOWLEDGE_DIR.is_dir()


def test_travel_documents_exist():
    documents = list(KNOWLEDGE_DIR.glob("*.txt"))

    assert len(documents) >= 5


def test_paris_document_exists():
    paris_file = KNOWLEDGE_DIR / "paris.txt"

    assert paris_file.exists()

    content = paris_file.read_text(encoding="utf-8")

    assert "Paris" in content
    assert "Eiffel Tower" in content