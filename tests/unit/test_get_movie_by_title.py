from app import app 

fake_movie_data = {
    "Ratafuillo": {"rating": 4},
    "Upies": {"rating": 3},
    "Cars on Rocks": {"rating": 2},
}

def test_search_existing_movie():
    client = app.test_client()
    response = client.post('/movies/search', data={'movie_title': 'Upies'})
    assert b'Upies' in response.data
    assert b'3' in response.data

def test_search_nonexistent_movie():
    client = app.test_client()
    response = client.post('/movies/search', data={'movie_title': 'NonExistentMovie'})
    assert b'No rating found for "NonExistentMovie".' in response.data