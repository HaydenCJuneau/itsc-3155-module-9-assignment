# TODO: Feature 4
from app import app, movie_repository

def test_get_single_movie():
    test_app = app.test_client()
    movie_repository.clear_db()
    movie = movie_repository.create_movie('Test Movie', 'Test Director', 5)

    response = movie_repository.get_movie_by_id(movie.movie_id)

    assert response is not None

def test_no_movie_exists():
    movie_repository.clear_db()
    
    response = movie_repository.get_movie_by_id(1)

    assert response is None
