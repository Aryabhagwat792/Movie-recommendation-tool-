# Movie Recommendation Project - Single File Version

# Movie data (like CSV but in code)
movies = [
    {"title": "Pretty Woman", "genre": "Romcom"},
    {"title": "About Time", "genre": "Romcom"},
    {"title": "Titanic", "genre": "Romance"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "Avengers: Endgame", "genre": "Action"},
    {"title": "John Wick", "genre": "Action"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "Inception", "genre": "Sci-Fi"}
]

# Welcome message
print("🎬 Welcome to Movie Recommendation! 🎬")

# Ask user for a genre
genre_input = input("Enter a genre (Romcom, Romance, Action, Sci-Fi): ").strip()

# Filter movies by genre
recommended = [movie['title'] for movie in movies if movie['genre'].lower() == genre_input.lower()]

# Display results
if recommended:
    print(f"\nMovies in {genre_input} genre:")
    for movie in recommended:
        print(f"- {movie}")
else:
    print(f"Sorry! No movies found for the genre '{genre_input}'.")
