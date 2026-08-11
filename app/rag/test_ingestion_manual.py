from app.rag.ingest import ingest_travel_knowledge


vector_store = ingest_travel_knowledge()

results = vector_store.similarity_search(
    "How can I travel around Paris?",
    k=2,
)

print("Retrieved:", len(results))

for result in results:
    print("\nSOURCE:", result.metadata["source"])
    print(result.page_content)