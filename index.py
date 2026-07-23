from vectordb import VectorDB
from chunking import chunk_with_overlap
from pprint import pprint

db = VectorDB()

with open("data/documents.txt","r",encoding="utf-8") as file:
    documents=file.readlines()

print("="*100)
pprint(documents)

documents=[doc.strip() for doc in documents if doc.strip()]

print("-" * 100)
pprint(documents)

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

    

print("*" * 100)
pprint(all_chunk)
pprint(all_metadatas)



print("Knowledge Base Created!")