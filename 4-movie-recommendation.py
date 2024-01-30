# Movie recommendation system

# Sample movie data (genre, title)
movies = [
    ("Comedy", "Superbad"),
    ("Action", "Avengers"),
    ("Drama", "The Godfather"),
    ("Drama","Hum Sath Sath Hain"),
    # ... more movies
]

# Function to recommend movies based on genre
def recommend_movies(genre):
    return [title for movie_genre, title in movies if movie_genre == genre]

# Main function for user interaction
def movie_recommender():
    user_genre = input("Enter your preferred movie genre (Comedy, Action, Drama, etc.): ")
    recommended = recommend_movies(user_genre)
    print("Movies you might like:", recommended)

# Running the recommender
movie_recommender()
