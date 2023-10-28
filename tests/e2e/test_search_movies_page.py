from app import app

#Fake movie data
fake_movie_data = {
    "Ratafuillo": {"rating": 4},
    "Upies": {"rating": 3},
    "Cars on Rocks": {"rating": 2},
}

def test_search_movies():
    client = app.test_client()

    get_response = client.get('/movies/search')
    assert get_response.status_code == 200
    
    post_response = client.post('/movies/search', data={'movie_title': 'Ratafuillo'})
    assert post_response.status_code == 200
    
    assert b'Search Movie Ratings' in post_response.data
    assert b'No rating found for "Ratafuillo".' in post_response.data
    
    # You can also test cases where no movie is found
    post_response_no_result = client.post('/movies/search', data={'movie_title': 'Gnomeo'})
    assert b'No rating found for "Gnomeo".' in post_response_no_result.data