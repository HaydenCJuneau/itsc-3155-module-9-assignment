# TODO: Feature 5
from app import app, movie_repository

def test_update_movie_data():
    movie_repository.clear_db()

    movie = movie_repository.create_movie("The fat and the furious", "Vin", 3)

    #with app.test_client() as client:
    updated_movie_data = {
            "title": "The frog and the furious",
            "director": "Bin",
            "rating": "5"
        }

    with app.test_client() as client:
        response = client.post(f'/movies/{movie.movie_id}', data=updated_movie_data)

    assert response.status_code == 302

    updated_movie = movie_repository.get_movie_by_id(movie.movie_id)

    assert updated_movie.title == updated_movie_data["title"]
    assert updated_movie.director == updated_movie_data["director"]
    assert updated_movie.rating == int(updated_movie_data["rating"]) 