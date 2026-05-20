import os
from flask import Flask, render_template_string, request
import pickle

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Resolve pickle paths in either root or model directory
movie_path = os.path.join(base_dir, 'movie.pkl')
if not os.path.exists(movie_path):
    movie_path = os.path.join(base_dir, 'model', 'movie.pkl')

similarity_path = os.path.join(base_dir, 'similarity.pkl')
if not os.path.exists(similarity_path):
    similarity_path = os.path.join(base_dir, 'model', 'similarity.pkl')

with open(movie_path, 'rb') as f:
    movies = pickle.load(f)
with open(similarity_path, 'rb') as f:
    similarity = pickle.load(f)

movie_titles = movies['title'].tolist()

PAGE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Movie Recommender System</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; background: #f9f9f9; }
      .container { max-width: 700px; margin: auto; background: #fff; padding: 2rem; border-radius: 12px; box-shadow: 0 0 20px rgba(0,0,0,0.08); }
      label, select, button { display: block; width: 100%; margin-bottom: 1rem; }
      select { padding: 0.75rem; font-size: 1rem; }
      button { padding: 0.85rem; font-size: 1rem; background: #007bff; color: white; border: none; border-radius: 6px; cursor: pointer; }
      button:hover { background: #0056d2; }
      .recommendations { margin-top: 1.5rem; }
      .recommendations ul { padding-left: 1.2rem; }
      .message { margin-top: 1rem; padding: 1rem; border-radius: 8px; background: #f0f4ff; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Movie Recommender System</h1>
      <form method="post">
        <label for="movie">Select a movie</label>
        <select name="movie" id="movie">
          {% for title in movie_titles %}
            <option value="{{ title }}" {% if title == selected %}selected{% endif %}>{{ title }}</option>
          {% endfor %}
        </select>
        <button type="submit">Recommend</button>
      </form>

      {% if selected is not none %}
        <div class="recommendations">
          <h2>Recommendations for: {{ selected }}</h2>
          {% if recommendations %}
            <ul>
              {% for rec in recommendations %}
                <li>{{ rec }}</li>
              {% endfor %}
            </ul>
          {% else %}
            <div class="message">No recommendations found for the selected movie.</div>
          {% endif %}
        </div>
      {% endif %}
    </div>
  </body>
</html>
'''



# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.strip()

    # Check if movie exists
    if movie_name not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie_name].index[0]

    distance = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda vector: vector[1]
    )

    recommended_movies = []

    # Skip first movie because it is the same movie
    for i in distance[1:6]:
        recommended_movies.append(movies.iloc[i[0]]['title'])

    return recommended_movies


@app.route('/', methods=['GET', 'POST'])
def home():
    selected = None
    recommendations = []

    if request.method == 'POST':
        selected = request.form.get('movie', '').strip()
        if selected:
            recommendations = recommend(selected)

    return render_template_string(
        PAGE,
        movie_titles=movie_titles,
        selected=selected,
        recommendations=recommendations,
    )


if __name__ == '__main__':
    app.run(debug=False)