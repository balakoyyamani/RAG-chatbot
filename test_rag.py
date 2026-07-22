from rag import ask
from vectordb import VectorDB

db=VectorDB()

documents = [
    "Java is an object-oriented programming language.",
    "Spring Boot helps build REST APIs.",
    "Docker is used for containerization.",
    "Python is popular for AI."
]

db.add_documents(documents)

answer = ask(
    "How do I build REST APIs?"
)

print(answer)