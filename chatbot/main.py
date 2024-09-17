from flask import Flask, render_template, request, jsonify
from chatbot.ai import get_chat_response

app = Flask(__name__)


@app.route("/chat")
def chat():
    return render_template("chat.html", message="Test")


@app.route("/api/chat", methods=["POST"])
def get_ai_response():
    body = request.get_json()
    prompt = body["prompt"] if body else None
    response = get_chat_response(prompt)
    return jsonify({"message": response})


app.run(debug=True)
