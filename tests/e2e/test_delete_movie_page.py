# TODO: Feature 6
import html 
from app import app, movie_repository

def test_movie_deleted(test_app):
    movie_repository.clear_db()

    movie_repository.create_movie('Barbie','Greta Gerwig',5)
    movie2 = movie_repository.create_movie('Red, White and Royal Blue','Matthew Lopez',5)

    movies = movie_repository.get_all_movies()

    movie_repository.delete_movie(movie2.movie_id)    

    movies = movie_repository.get_all_movies()
    
    assert len(movies) == 1 

    response = test_app.post('movies/{{ movie2.movie_id}}/delete')
    assert response.status_code == 404
