# Duplicate Question Detection System

## Overview

Duplicate Question Detection is a Natural Language Processing (NLP) and Machine Learning project that identifies whether two questions have the same meaning, even when they are written differently.

The system combines advanced text preprocessing, feature engineering, TF-IDF vectorization, and an XGBoost classifier to determine if two questions are duplicates.

### Example

**Question 1:** How can I learn Python?

**Question 2:** What is the best way to learn Python?

**Prediction:** Duplicate Questions 

---

## Features

* Text preprocessing and cleaning
* NLP-based feature engineering
* Fuzzy string matching
* TF-IDF vectorization
* XGBoost classifier
* Flask REST API backend
* Interactive web interface
* Real-time duplicate question prediction
* Confidence score prediction

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

This project uses the Quora Question Pairs Dataset containing over **404,000 question pairs**.

### Dataset Information

* Total Samples: ~404,000
* Target Variable:

  * 1 → Duplicate Questions
  * 0 → Non-Duplicate Questions

Dataset Columns:

* question1
* question2
* is_duplicate

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
* Gunicorn

### Data Processing

* NumPy
* Pandas
* SciPy

### Deployment

* Render
* GitHub

---

## Feature Engineering

The following features are extracted from question pairs:

### Basic Features

* Question Length
* Number of Words
* Length Difference
* Word Count Difference

### Word Similarity Features

* Common Words
* Word Share
* Jaccard Similarity

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

---

## TF-IDF Vectorization

TF-IDF is used to convert textual information into numerical vectors.

Configuration:

```python
TfidfVectorizer(
    max_features=15000,
    stop_words="english",
    ngram_range=(1,2)
)
```

---

## Model Training

### Models Evaluated

#### Random Forest Classifier

Accuracy: ~75%

#### XGBoost Classifier

Accuracy: ~81.93%

The XGBoost model achieved the best performance and was selected for deployment.

---

## Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 81.93% |
| Precision | 81%    |
| Recall    | 80%    |
| F1 Score  | 81%    |

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
│   │   ├── scaler.pkl
│   │   └── feature_cols.pkl
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
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/bstar042005/Duplicate-Question-Detection.git
```

```bash
cd Duplicate-Question-Detection
```

### Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Run Backend Server

```bash
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
  "duplicate": 1,
  "confidence": 92.45
}
```

Where:

* 1 → Duplicate
* 0 → Non-Duplicate
* confidence → Model confidence percentage

---

## Frontend

The project includes a simple and responsive frontend built using:

* HTML
* CSS
* JavaScript

Users can enter two questions and receive real-time duplicate detection results from the Flask API.

---

## Author

**Bhavya Vaish**
