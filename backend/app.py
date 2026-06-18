from flask import Flask, request, jsonify
from flask_cors import CORS

import pickle
import pandas as pd
from scipy.sparse import hstack

from utils.preprocessing import preprocess
from utils.feature_engineering import build_features

app = Flask(__name__)
CORS(app)

# Load model files
with open("model/duplicate_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

feature_cols = [
    "q1_len",
    "q2_len",
    "q1_num_words",
    "q2_num_words",
    "common_words",
    "word_share",
    "cwc_min",
    "cwc_max",
    "csc_min",
    "csc_max",
    "ctc_min",
    "ctc_max",
    "first_word_eq",
    "last_word_eq",
    "fuzz_ratio",
    "fuzz_partial_ratio",
    "token_sort_ratio",
    "token_set_ratio",
    "len_diff",
    "word_count_diff",
    "jaccard",
]


@app.route("/")
def home():
    return jsonify({
        "message": "Duplicate Question Detection API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        q1 = data["question1"]
        q2 = data["question2"]

        q1 = preprocess(q1)
        q2 = preprocess(q2)

        feature_dict = build_features(q1, q2)

        numerical_features = pd.DataFrame([feature_dict])
        numerical_features = numerical_features[feature_cols]

        numerical_features_scaled = scaler.transform(
            numerical_features
        )

        combined_text = q1 + " " + q2

        text_features = vectorizer.transform(
            [combined_text]
        )

        final_features = hstack(
            [
                text_features,
                numerical_features_scaled
            ]
        )

        prediction = int(
            model.predict(final_features)[0]
        )

        probability = float(
            model.predict_proba(final_features)[0][1]
        )

        return jsonify({
            "duplicate": prediction,
            "confidence": round(probability * 100, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )