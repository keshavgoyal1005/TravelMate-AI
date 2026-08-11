from app.rag.chain import create_rag_chain


rag_chain = create_rag_chain()

question = "What transportation is available in Paris?"

answer = rag_chain(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)