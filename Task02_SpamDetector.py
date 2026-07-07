# Task 02 - Spam Message Detection
# Internship: IncodeVision
# Author: Devendra (bhoomijn)
# Description: Detects spam vs ham messages using Naive Bayes and TF-IDF.

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

def spam_detector():
    # 📂 Dataset: SMS Spam Collection (can be replaced with your own CSV)
    # Format: label (spam/ham), message
    data = pd.read_csv("spam.csv", encoding="latin-1")
    data = data[['v1','v2']]
    data.columns = ['label','message']

    # 🔄 Convert labels to numeric
    data['label'] = data['label'].map({'ham':0, 'spam':1})

    # ✂️ Split data
    X_train, X_test, y_train, y_test = train_test_split(
        data['message'], data['label'], test_size=0.2, random_state=42
    )

    # 🧮 Text vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # 🤖 Model training
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)

    # ✅ Evaluation
    y_pred = model.predict(X_test_tfidf)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    # 🔍 Example prediction
    sample = ["Congratulations! You won a free lottery ticket"]
    sample_tfidf = vectorizer.transform(sample)
    print("\nSample Prediction:", "Spam" if model.predict(sample_tfidf)[0] else "Ham")

if __name__ == "__main__":
    spam_detector()
