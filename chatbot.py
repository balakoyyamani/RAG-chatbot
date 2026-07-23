from rag import ask

print("=" * 50)
print("Production RAG Chatbot")
print("=" * 50)

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":

        print("Goodbye!")

        break

    if not question.strip():

        print("Please ask something.")

        continue

    result = ask(question)

    print(f"\nAI : {result["answer"]}")
    for source in result["sources"]:
        print(f"= {source}")