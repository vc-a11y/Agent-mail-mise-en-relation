import os, json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt   = data.get("prompt", "")
    messages = data.get("messages", [])
    if not prompt and not messages:
        return jsonify({"error": "prompt ou messages requis"}), 400
    try:
        client = get_client()
        msgs = messages if messages else [{"role":"user","content":prompt}]
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1200,
            system="Tu es expert en communication B2B pour organismes de formation en alternance. Tu rédiges des mails de mise en relation percutants, humains et efficaces pour convaincre des entreprises d'accueillir des alternants. Réponds toujours en français.",
            messages=msgs
        )
        return jsonify({"text": response.content[0].text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
