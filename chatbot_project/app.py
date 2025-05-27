from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

responses = {
    "order_tracking": ["Your order is on the way!", "Tracking ID: 1234567890"],
    "return_request": ["Please visit our return portal to initiate the process."],
    "product_info": ["The iPhone 14 features A16 chip and a new camera system."],
    "payment_issue": ["We noticed a failed transaction. Please try again or use a different method."]
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    intent = detect_intent(user_input)
    return jsonify({"response": random.choice(responses.get(intent, ["I'm not sure. Can I connect you to a human?"]))})

def detect_intent(message):
    if "track" in message or "package" in message:
        return "order_tracking"
    elif "return" in message:
        return "return_request"
    elif "iphone" in message or "product" in message:
        return "product_info"
    elif "pay" in message:
        return "payment_issue"
    else:
        return "unknown"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
