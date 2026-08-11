from app.rag.embeddings import get_embedding_model


embedding_model = get_embedding_model()

text = "Paris has an extensive Metro system."

vector = embedding_model.embed_query(text)

print("Vector dimensions:", len(vector))
print("First 10 values:", vector[:10])