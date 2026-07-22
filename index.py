from vectordb import VectorDB
from chunking import chunk_with_overlap

db = VectorDB()

with open("data/documents.txt","r",encoding="utf-8") as file:
    documents=file.readlines()

print("="*100)
print(documents)

documents=[doc.strip() for doc in documents if doc.strip()]

print("-" * 100)
print(documents)

all_chunk=[]

for doc in documents:
    chunk=chunk_with_overlap(doc)
    all_chunk.extend(chunk)

print("*" * 100)
print(all_chunk)

db.add_documents(all_chunk)

print("Knowledge Base Created!")