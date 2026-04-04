import pandas as pd
import ast

print("📂 Loading dataset...")

# Load dataset
try:
    movies = pd.read_csv("tmdb_5000_movies.csv.zip")
except FileNotFoundError:
    print("❌ ERROR: tmdb_5000_movies.csv.zip not found!")
    exit()

# Keep only required columns
movies = movies[["title", "genres"]]

# Convert string genres to list
def extract_genres(text):
    genres_list = []
    try:
        for item in ast.literal_eval(text):
            genres_list.append(item["name"].lower())
    except:
        pass
    return genres_list

movies["genres"] = movies["genres"].apply(extract_genres)

print("✅ Dataset ready!")

# Recommendation function based on genre
def recommend_by_genre(user_input):
    user_input = user_input.lower().strip()

    matched_movies = []

    for i in range(len(movies)):
        genres = movies.iloc[i]["genres"]

        # Match if any word in input matches genres
        if any(word in genres for word in user_input.split()):
            matched_movies.append(movies.iloc[i]["title"])

    if len(matched_movies) == 0:
        print("❌ No movies found for this genre.")
    else:
        print(f"\n🎬 Movies under '{user_input}':\n")
        for movie in matched_movies[:10]:  # limit to 10
            print(movie)

# Main loop
print("\n🎥 Genre-Based Recommendation System Ready!")

while True:
    user_input = input("\nEnter a genre (e.g., romance, comedy, action) or 'exit': ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    recommend_by_genre(user_input)