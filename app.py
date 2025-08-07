from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Gemini API Key
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define instruction prefix
INSTRUCTION = (
    "You are WaterBot, a helpful assistant that only answers questions about water conservation, "
    "sanitation, and hygiene. If the question is not about those topics, politely respond that you are "
    "limited to water-related questions only.\n\n"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    try:
        # Add instruction prefix to user input
        full_prompt = INSTRUCTION + "User: " + user_input

        # Generate response
        response = model.generate_content(full_prompt)
        answer = response.text.strip()

        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

