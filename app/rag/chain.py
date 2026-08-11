from langchain_core.documents import Document

from app.rag.llm import get_llm
from app.rag.prompts import RAG_PROMPT
from app.rag.retriever import get_travel_retriever


def format_documents(documents: list[Document]) -> str:
    return "\n\n".join(
        document.page_content
        for document in documents
    )


def create_rag_chain():
    retriever = get_travel_retriever()
    llm = get_llm()

    def answer_question(question: str) -> str:
        documents = retriever.invoke(question)

        context = format_documents(documents)

        prompt = RAG_PROMPT.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        response = llm.invoke(prompt)

        return response.content

    return answer_question