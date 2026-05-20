# Movie Recommendation System

This repository contains a Movie Recommendation System that uses the TMDB dataset (`data/tmdb_5000_movies.csv`). It includes data exploration, model training (content-based recommender), and a small local app to serve recommendations.

## Table of Contents
- Features
- Tech Stack
- Installation
- Usage
- Dataset
- Future Enhancements
- Contact

## Features
- Content-based recommendations using movie metadata (genres, overview, keywords).
- Model training and serialization for fast inference.
- Local app (`app.py`) to request recommendations by movie title.
- Jupyter notebook for exploration and experimentation (`model/movie.ipynb`).
- Simple, responsive UI (if `app.py` provides a web front-end).

## Tech Stack
- Python 3.8+
- pandas, numpy
- scikit-learn
- Flask (or your chosen web framework)
- Jupyter Notebook

## Installation
1. Clone the repository:

```bash
git clone <your-repo-url>
cd movie-recommendation-system
```

2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies (create `requirements.txt` or run):

```powershell
pip install pandas numpy scikit-learn flask jupyter
```

4. Ensure the dataset is present at `data/tmdb_5000_movies.csv`.

## Usage
- Train the model (if you need to rebuild):

```powershell
python model.py
```

- Run the app (serves recommendations):

```powershell
python app.py
```

- Open `http://localhost:5000` (or the port your `app.py` uses) and query recommendations by movie title.

## Dataset
- File: `data/tmdb_5000_movies.csv`
- Used fields: `title`, `overview`, `genres`, `keywords`, `cast` (if present) to compute similarity features.
- If you need a database-backed version, we can add scripts to load data into MySQL/Postgres.

## Future Enhancements
- Add collaborative filtering (user-based or item-based) to support personalized recommendations.
- Provide an API endpoint for batch recommendations.
- Add caching and model versioning.
- Improve UI and add user accounts to save favorites.

## Contact
- Author: (add your name or contact)
- GitHub: (add your GitHub profile)

If you want, I can also:
- generate a `requirements.txt`,
- add example API endpoints in `app.py`,
- or produce a small seed dataset and example requests. Tell me which next.
