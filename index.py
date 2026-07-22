from vectordb import VectorDB

db = VectorDB()

with open(
    "data/documents.txt",
    "r",
    encoding="utf-8"
) as file:

    documents = file.readlines()

    
documents = [
    doc.strip()

    for doc in documents

    if doc.strip()
]

db.add_documents(documents)

print("Knowledge Base Created!")