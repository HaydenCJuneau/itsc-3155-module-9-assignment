# TODO: Feature 4
from app import app, movie_repository

client = app.test_client()

def test_get_single_movie_valid():
    movie_repository.clear_db()
    # Create dummy data
    movie1 = movie_repository.create_movie('Bros of the Ring', 'Pete J', 5)
    movie2 = movie_repository.create_movie('The Two Lit Towers', 'Viggo', 4)
    movie3 = movie_repository.create_movie('Return of the Bro', 'Sir Ian', 5)

    # Go to page
    response = client.get(f'/movies/{movie1.movie_id}')

    data = response.data.decode('utf-8')

    # Test movie 1 stuff is there and nothing else
    assert response.status_code == 200
    assert f'<th scope="row">{movie1.movie_id}</th>' in data
    assert f'<td>{movie1.title}</td>' in data
    assert f'<td>{movie1.director}</td>' in data
    assert f'<td>{movie1.rating}</td>' in data
    assert f'<td>{movie2.title}</td>' not in data
    assert f'<td>{movie2.director}</td>' not in data
    assert f'<td>{movie3.title}</td>' not in data
    assert f'<td>{movie3.director}</td>' not in data

    # Go to movie 2 page
    response = client.get(f'/movies/{movie2.movie_id}')

    data = response.data.decode('utf-8')

    # Test movie 2 stuff is there and nothing else
    assert response.status_code == 200
    assert f'<th scope="row">{movie2.movie_id}</th>' in data
    assert f'<td>{movie2.title}</td>' in data
    assert f'<td>{movie2.director}</td>' in data
    assert f'<td>{movie2.rating}</td>' in data
    assert f'<td>{movie1.title}</td>' not in data
    assert f'<td>{movie1.director}</td>' not in data
    assert f'<td>{movie3.title}</td>' not in data
    assert f'<td>{movie3.director}</td>' not in data

    # Go to movie 3 page
    response = client.get(f'/movies/{movie3.movie_id}')

    data = response.data.decode('utf-8')

    # Test movie 3 stuff is there and nothing else
    assert response.status_code == 200
    assert f'<th scope="row">{movie3.movie_id}</th>' in data
    assert f'<td>{movie3.title}</td>' in data
    assert f'<td>{movie3.director}</td>' in data
    assert f'<td>{movie3.rating}</td>' in data
    assert f'<td>{movie1.title}</td>' not in data
    assert f'<td>{movie1.director}</td>' not in data
    assert f'<td>{movie2.title}</td>' not in data
    assert f'<td>{movie2.director}</td>' not in data

def test_get_single_movie_invalid():
    movie_repository.clear_db()

    response = client.get('/movies/4356')

    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert f'<td></td>' in data
