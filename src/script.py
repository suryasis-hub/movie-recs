import pandas as pd

# Load both CSVs
movies = pd.read_csv("../data/movies.csv")     # movieId, title, genres
ratings = pd.read_csv("../data/ratings.csv") 
df = ratings.merge(movies, on="movieId", how="inner")
df = df.drop(columns=["timestamp"])
df.to_csv("../data/ratings_with_movies.csv", index=False)
print(f"Saved merged dataset with {len(df)} rows.")