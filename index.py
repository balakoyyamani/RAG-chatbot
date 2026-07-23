from vectordb import VectorDB
from chunking import chunk_with_overlap
from pprint import pprint

db = VectorDB()
db.reset_collection()

with open("data/documents.txt","r",encoding="utf-8") as file:
    documents=file.readlines()

documents=[doc.strip() for doc in documents if doc.strip()]


all_chunk=[]
all_metadatas=[]

for index,doc in enumerate(documents):
    chunks=chunk_with_overlap(doc)
    for chunk_number,chunk in enumerate(chunks):
        all_chunk.append(chunk)
        all_metadatas.append({

            "source":"documents.txt",

            "document":index,

            "chunk":chunk_number

        })

db.add_documents(all_chunk,all_metadatas)

print("Knowledge Base Created!")