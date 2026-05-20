import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_candidates = [
    os.path.join(base_dir, 'data', 'tmdb_5000_movies.csv'),
    os.path.join(base_dir, 'tmdb_5000_movies.csv'),
    os.path.join(base_dir, 'data', 'top10K-TMDB-movies.csv'),
    os.path.join(base_dir, 'top10K-TMDB-movies.csv'),
]

dataset_path = None
for path in csv_candidates:
    if os.path.exists(path):
        dataset_path = path
        break

if dataset_path is None:
    raise FileNotFoundError(
        'Could not find the dataset. Place tmdb_5000_movies.csv or top10K-TMDB-movies.csv in the project root or data/ folder.'
    )

# Load dataset

df = pd.read_csv(dataset_path)

# Select important columns
available_text_columns = [
    column_name for column_name in ['overview', 'genres', 'genre', 'keywords', 'tagline']
    if column_name in df.columns
]

movies = df.loc[:, ['id', 'title', *available_text_columns]].copy()

# Create tags from the columns that exist in this dataset
tag_source_columns = [column_name for column_name in ['overview', 'genres', 'genre', 'keywords', 'tagline']
                      if column_name in movies.columns]
movies.loc[:, 'tag'] = movies[tag_source_columns].fillna('').astype(str).agg(' '.join, axis=1)

# Remove unwanted columns
new_data = movies.drop(columns=available_text_columns)

# Convert text into vectors
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(new_data['tag'].values.astype('U')).toarray()

# Calculate similarity
similarity = cosine_similarity(vector)

# Save files
pickle.dump(new_data, open(os.path.join(base_dir, 'movie.pkl'), 'wb'))
pickle.dump(similarity, open(os.path.join(base_dir, 'similarity.pkl'), 'wb'))

print('Files Saved Successfully')