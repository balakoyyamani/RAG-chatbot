from pdf_loader import load_pdfs

folder="data"
documents=load_pdfs(folder)

for document in documents:
    print(f"pdf name : {document["file"]}")
    print("-" * 40)

    for page in document["pages"]:
        print(f"page no :{page["page"]}")
        print(page["text"][:10])
        print()