from app.rag.llm import get_llm


llm = get_llm()

response = llm.invoke(
    "Explain what RAG is in one sentence."
)

print(response.content)