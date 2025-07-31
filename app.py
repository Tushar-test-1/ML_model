from flask import Flask, request, jsonify

app = Flask(__name__)

# Example ML-style mapping (you can replace or expand this later)
prediction_map = {
    "P123": 78.5,
    "P124": 91.0,
    "P125": 63.2,
    "A111": 82.0,
    "B222": 69.5
}

@app.route('/')
def home():
    return "ML Prediction API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_id = data.get('id', '').strip()

    # Lookup prediction from predefined map
    prediction = prediction_map.get(input_id, 0.0)  # Return 0.0 if ID not found

    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
