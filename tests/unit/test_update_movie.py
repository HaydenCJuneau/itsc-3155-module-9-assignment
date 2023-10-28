from app import app, movie_repository

def test_update_movie_data():
    movie_repository.clear_db()

    # Create a movie and get its movie_id
    movie = movie_repository.create_movie("The fat and the furious", "Vin", 3)
    movie_id = movie.movie_id

    # Define the updated movie data
    updated_movie_data = {
        "title": "The frog and the furious",
        "director": "Bin",
        "rating": "5"
    }

    with app.test_client() as client:
        # Use the proper HTTP method for updating (typically PUT or PATCH)
        response = client.put(f'/movies/{movie_id}', data=updated_movie_data)

    assert response.status_code == 405

    updated_movie = movie_repository.get_movie_by_id(movie_id)

    assert updated_movie.title == updated_movie_data["title"]
    assert updated_movie.director == updated_movie_data["director"]
    assert updated_movie.rating == int(updated_movie_data["rating"])