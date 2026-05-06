from flask import Flask, request, jsonify
from google import genai
import os

app = Flask(__name__)

API_KEY = os.environ.get("GEMINI_API_KEY")
STORE_ID = "fileSearchStores/repositoriomarfel-s2bp5sj0nwhr"

client = genai.Client(api_key=API_KEY)

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    pergunta = data.get("question", "")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=pergunta,
        config=genai.types.GenerateContentConfig(
            tools=[
                genai.types.Tool(
                    file_search=genai.types.FileSearchTool(
                        file_search_stores=[STORE_ID]
                    )
                )
            ]
        )
    )

    return jsonify({"answer": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
