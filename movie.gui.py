import tkinter as tk
from tkinter import messagebox

# Movie data stored directly in code
movies = [
    {"title": "Pretty Woman", "genre": "Romcom"},
    {"title": "About Time", "genre": "Romance"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "Avengers: Endgame", "genre": "Action"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "Crazy Rich Asians", "genre": "Romcom"},
    {"title": "Inception", "genre": "Sci-Fi"},
]

# Function to get recommendations
def recommend_movies():
    genre_input = genre_entry.get().strip()
    recommended = [movie['title'] for movie in movies if movie['genre'].lower() == genre_input.lower()]
    
    if recommended:
        result_text = "\n".join(recommended)
    else:
        result_text = "No movies found for this genre."
    
    result_label.config(text=result_text)

# Create GUI window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("400x400")

# GUI Widgets
tk.Label(root, text="Enter a genre (Romcom, Romance, Action, Sci-Fi):").pack(pady=10)
genre_entry = tk.Entry(root)
genre_entry.pack(pady=5)

tk.Button(root, text="Get Recommendations", command=recommend_movies).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()
