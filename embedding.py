from config import client,embedding_model

def get_embedding(text):
    try:
        response=client.models.embed_content(
            model=embedding_model,
            contents=text
        )
        return response.embeddings[0].values
    except Exception as e:
        print(e)
        return None

def get_embeddings(texts):
    try:
        response=client.models.embed_content(
            model=embedding_model,
            contents=texts
        )
        vectors=[embed.values for embed in response.embeddings]
        return vectors
    except Exception as e:
        print(e)
        return None