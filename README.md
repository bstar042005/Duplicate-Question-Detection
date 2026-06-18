# Duplicate Question Detection System

## Overview

Duplicate Question Detection is a Natural Language Processing (NLP) project that identifies whether two questions have the same meaning, even if they are phrased differently.

The system uses text preprocessing, feature engineering, TF-IDF vectorization, and XGBoost classification to predict whether a pair of questions are duplicates.

Example:

**Question 1:** How can I learn Python?

**Question 2:** What is the best way to learn Python?

**Prediction:** Duplicate Questions ✅

---

## Features

* Text preprocessing and cleaning
* Feature engineering using NLP techniques
* Fuzzy string matching features
* TF-IDF vectorization
* XGBoost classifier
* Flask REST API backend
* Interactive web interface
* Real-time duplicate question prediction

---

## Project Architecture

```text
User Input
     │
     ▼
Frontend (HTML, CSS, JavaScript)
     │
     ▼
Flask API
     │
     ▼
Text Preprocessing
     │
     ▼
Feature Engineering
     │
     ▼
TF-IDF Vectorization
     │
     ▼
XGBoost Model
     │
     ▼
Prediction Result
```

---

## Dataset

The project uses the Quora Question Pairs Dataset containing over 400,000 question pairs.

Dataset Information:

* Total Samples: ~404,000
* Target Variable:

  * 1 → Duplicate Questions
  * 0 → Non-Duplicate Questions

The dataset consists of:

* Question 1
* Question 2
* Duplicate Label

---

## Technologies Used

### Programming Languages

* Python
* JavaScript
* HTML
* CSS

### Machine Learning & NLP

* Scikit-Learn
* XGBoost
* NLTK
* TF-IDF Vectorizer
* FuzzyWuzzy

### Backend

* Flask
* Flask-CORS

### Data Processing

* NumPy
* Pandas
* SciPy

---

## Feature Engineering

The following features were extracted from question pairs:

### Basic Features

* Question Length
* Number of Words
* Common Words
* Word Share

### Token-Based Features

* Common Word Count Ratios
* Common Stopword Ratios
* Common Token Ratios
* First Word Match
* Last Word Match

### Fuzzy Matching Features

* Fuzz Ratio
* Partial Ratio
* Token Sort Ratio
* Token Set Ratio

### TF-IDF Features

TF-IDF vectorization is used to convert textual information into numerical vectors for model training.

---

## Model Training

### Models Evaluated

#### Random Forest Classifier

* Accuracy: ~75%

#### XGBoost Classifier

* Accuracy: ~80.5%

The XGBoost model achieved the best performance and was selected for deployment.

---

## Project Structure

```text
Duplicate-Question-Detection
│
├── backend
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── model
│   │   ├── duplicate_model.pkl
│   │   ├── vectorizer.pkl
│   │   └── scaler.pkl
│   │
│   └── utils
│       ├── preprocessing.py
│       └── feature_engineering.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── notebook
│   └── model_training.ipynb
│
├── dataset
│
├── README.md
└── requirements.txt
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Duplicate-Question-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Server

```bash
cd backend
python app.py
```

Server will start at:

```text
http://127.0.0.1:5000
```

---

## API Endpoint

### Predict Duplicate Questions

**Endpoint**

```http
POST /predict
```

### Request Body

```json
{
  "question1": "How can I learn Python?",
  "question2": "What is the best way to learn Python?"
}
```

### Response

```json
{
  "duplicate": 1
}
```

Where:

* 1 → Duplicate
* 0 → Not Duplicate

---

## Results

| Model            | Accuracy |
| ---------------- | -------- |
| Random Forest    | ~75%     |
| XGBoost + TF-IDF | ~80.5%   |

---

## Author

**Bhavya Vaish**

