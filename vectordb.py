import chromadb
from uuid import uuid4
from embedding import get_embedding,get_embeddings

class VectorDB:
    def __init__(self):
        self.client=chromadb.PersistentClient(
            path="database"
        )
        self.collections=self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def reset_collection(self):
        try:
            self.client.delete_collection(name="knowledge_base")
            print("Database Deleted")
        except:
            print("collection doesnt exist. Creating new one.")

        self.collections=self.client.create_collection(name="knowledge_base")
        print("New collection is ready")

    def add_documents(self,documents,metadatas):
        vectors=get_embeddings(documents)
        ids=[str(uuid4()) for i in range(len(documents))]
        self.collections.add(
            ids=ids,
            documents=documents,
            embeddings=vectors,
            metadatas=metadatas
        )

    def search(self,question,n=3):
        query_vector=[get_embedding(question)]
        results=self.collections.query(
            query_embeddings=query_vector,
            n_results=n
        )

        return results