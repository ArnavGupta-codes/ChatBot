from flask import Flask, render_template, send_from_directory, request, jsonify
from main import generate_answer  # Adapted RAG function from main.py

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Inductions_Catalogue.pdf")
def catalogue_pdf():
    return send_from_directory("static", "Inductions_Catalogue.pdf")

@app.route("/ask", methods=["POST"])
def ask():
    user_prompt = request.json.get("prompt")
    history = request.json.get("history", [])
    from main import embed_model, client, retrieve_relevant_chunks, generate_answer
    # Build a context string from the last 4-5 messages
    history_context = "\n".join([
        ("You: " if h["role"] == "user" else "Bot: ") + h["content"] for h in history[-5:]
    ])
    # Combine the chat history and the current prompt for retrieval
    retrieval_query = history_context + ("\nYou: " if history_context else "") + user_prompt
    relevant_chunks = retrieve_relevant_chunks(retrieval_query, embed_model, client)
    # Pass both the chat history and the answer context to the LLM
    answer = generate_answer(user_prompt, relevant_chunks, history_context=history_context)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
