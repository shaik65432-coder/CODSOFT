import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
movies = pd.read_csv("movies.csv")


# Convert text data into numbers
cv = CountVectorizer()

count_matrix = cv.fit_transform(movies["genre"])


# Calculate similarity
similarity = cosine_similarity(count_matrix)


# Recommendation function
def recommend(movie_name):

    if movie_name not in movies["movie"].values:
        print("Movie not found in database.")
        return

    # Get movie index
    movie_index = movies[movies["movie"] == movie_name].index[0]

    # Similar movies
    scores = list(enumerate(similarity[movie_index]))

    # Sort movies
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:\n")

    # Display top recommendations
    for movie in sorted_scores[1:4]:

        index = movie[0]

        print(movies.iloc[index]["movie"])


# User input
movie_name = input("Enter a movie name: ")

recommend(movie_name)