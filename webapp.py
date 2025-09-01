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
    from main import embed_model, client, retrieve_relevant_chunks
    relevant_chunks = retrieve_relevant_chunks(user_prompt, embed_model, client)
    answer = generate_answer(user_prompt, relevant_chunks)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
