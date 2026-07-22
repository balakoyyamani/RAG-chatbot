from config import chat_model,client

response=client.models.generate_content(
    model=chat_model,
    contents="Say Hello"
)
print(response.text)