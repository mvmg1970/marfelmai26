from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    pergunta = data.get("question", "")

    if not pergunta:
        return jsonify({"error": "Pergunta não informada"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=pergunta
        )
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
