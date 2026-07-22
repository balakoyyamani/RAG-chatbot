from vectordb import VectorDB

db=VectorDB()

docs = [

    "Java Programming",

    "Spring Boot REST APIs",

    "Python AI",

    "Docker Containers"
]

db.add_documents(docs)
results=db.search("How do I create REST API's?")

print(results["documents"][0])