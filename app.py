from flask import Flask, request, jsonify
from rag import ask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Production RAG Chatbot API",
        "status": "Running"
    }

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "error": "Question is required."
        }), 400

    answer = ask(question)

    return jsonify({
        "question": question,
        "answer": answer
    })

if __name__ == "__main__":
    app.run(debug=True)