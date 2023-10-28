# TODO: Feature 6
from app import app, movie_repository
import pytest


def test_movie_id_not_found():
    movie_repository.clear_db()
    with app.test_client() as client:
        movie = movie_repository.create_movie('Barbie','Greta Gerwig',5)
        movie_repository.delete_movie(movie.movie_id)

        response = client.get('/movies/<int:movie_id>/delete')

    assert response.status_code == 404



def test_delete_existing_movie():
    movie_repository.clear_db()
    movie = movie_repository.create_movie('Barbie','Greta Gerwig',5)
    movie_repository.delete_movie(movie.movie_id) 
    movies = movie_repository.get_all_movies()

    assert len(movies) == 0 
 




        
