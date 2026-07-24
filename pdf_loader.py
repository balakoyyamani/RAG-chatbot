import fitz
import os
from pprint import pprint

def extract_pdf(path):
    pdf=fitz.open(path)
    pages=[]
    for page_no,page in enumerate(pdf):
        pages.append({
            "text":page.get_text(),
            "page":page_no+1
        }        
        )
    pdf.close()
    return pages

def load_pdfs(folder):
    pdf_files=[
        file
        for file in os.listdir(folder)
        if file.endswith(".pdf")
    ]
    documents=[]

    for pdf in pdf_files:
        path=os.path.join(folder,pdf)
        documents.append({
            "file":pdf,
            "pages":extract_pdf(path)
        })
    return documents