from vectordb import VectorDB
from chunking import chunk_with_overlap
from pdf_loader import load_pdfs
from pprint import pprint

db = VectorDB()
db.reset_collection()

folder="data"
documents=load_pdfs(folder)

all_chunk=[]
all_metadatas=[]

for document in documents:
    file_name=document["file"]
    for pages in document["pages"]:
        page_no=pages["page"]
        text=pages["text"]
        chunks=chunk_with_overlap(text)
        for chunk_no,chunk in enumerate(chunks):
            all_chunk.append(chunk)
            all_metadatas.append({
                "source":file_name,
                "page":page_no,
                "chunk":chunk_no + 1
            })

db.add_documents(all_chunk,all_metadatas)

print("Knowledge Base Created!")