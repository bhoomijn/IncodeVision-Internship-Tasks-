# Task 04 - AI Resume Screening System
# Internship: IncodeVision
# Author: Devendra (bhoomijn)
# Description: Matches resumes with job descriptions using NLP similarity.

import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def resume_screening():
    # 📂 Sample resumes (can be replaced with actual text files)
    resumes = {
        "Resume1": "Experienced Python developer with knowledge of machine learning and data analysis.",
        "Resume2": "Frontend developer skilled in HTML, CSS, JavaScript, and React.",
        "Resume3": "AI/ML enthusiast with experience in NLP, TensorFlow, and deep learning projects."
    }

    # 📌 Job description
    job_description = "Looking for an AI/ML engineer skilled in Python, NLP, and machine learning."

    # 🧮 Vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    docs = list(resumes.values()) + [job_description]
    tfidf_matrix = vectorizer.fit_transform(docs)

    # 🔄 Similarity calculation
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # 📊 Results
    print("\nJob Description:", job_description)
    print("\nResume Screening Results:")
    for idx, (name, text) in enumerate(resumes.items()):
        print(f"{name}: {similarity_scores[0][idx]:.2f} similarity")

    # ✅ Best match
    best_match_idx = similarity_scores[0].argmax()
    best_resume = list(resumes.keys())[best_match_idx]
    print(f"\nBest Match: {best_resume}")

if __name__ == "__main__":
    resume_screening()
