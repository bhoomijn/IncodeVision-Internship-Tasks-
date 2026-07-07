# Task 03 - Movie Recommendation System
# Internship: IncodeVision
# Author: Devendra (bhoomijn)
# Description: Recommends movies based on similarity of genres/categories using cosine similarity.

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def movie_recommender():
    # 📂 Sample dataset (can be replaced with larger dataset)
    data = {
        'title': [
            'The Matrix', 'John Wick', 'Avengers', 
            'Titanic', 'The Notebook', 'Interstellar'
        ],
        'genre': [
            'Action Sci-Fi', 'Action Thriller', 'Action Superhero',
            'Romance Drama', 'Romance', 'Sci-Fi Adventure'
        ]
    }

    df = pd.DataFrame(data)

    # 🔄 Convert genres into vectors
    vectorizer = CountVectorizer()
    genre_matrix = vectorizer.fit_transform(df['genre'])

    # 🧮 Compute cosine similarity
    similarity = cosine_similarity(genre_matrix)

    # 📌 Function to recommend movies
    def recommend(movie):
        if movie not in df['title'].values:
            print("Movie not found in dataset.")
            return
        idx = df[df['title'] == movie].index[0]
        scores = list(enumerate(similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)
        print(f"\nRecommended movies similar to '{movie}':")
        for i in scores[1:4]:  # top 3 recommendations
            print("-", df.iloc[i[0]]['title'])

    # 🔍 Example usage
    recommend("The Matrix")
    recommend("Titanic")

if __name__ == "__main__":
    movie_recommender()
