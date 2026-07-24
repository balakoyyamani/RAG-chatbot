from config import  chat_model,client
from vectordb import VectorDB

db=VectorDB()

def ask(question):
    results=db.search(question)

    # context="\n\n".join(results["documents"][0])

    documents=results["documents"][0]
    metadatas=results["metadatas"][0]
    context=""
    sources=[]

    for doc,meta in zip(documents,metadatas):
        context+=doc+"\n\n"
        source={
            "file":meta["source"],
            "page":meta["page"]
        }
        if source not in sources:
            sources.append(source)

    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY using the context below.

    If the answer is not present in the context,
    reply:

    "I couldn't find that information."

    Context:

    {context}

    Question:

    {question}
    """
    response=client.models.generate_content(
        model=chat_model,
        contents=prompt
    )
    return {
        "answer":response.text,
        "sources":sources
    }