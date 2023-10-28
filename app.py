from flask import Flask, redirect, render_template, request,abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, list_movies=movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie(): 
    title = request.form.get('title', '').strip()
    director = request.form.get('director', '').strip()
    rating_str = request.form.get('rating', None)
    
    if not title or not director or not rating_str:
        return "All fields are required!", 400 

    try:
        rating = int(rating_str)
    except ValueError:
        return "Invalid rating!", 400
    
    if rating < 1 or rating > 5:
        return "Rating must be between 1 and 5!", 400

    movie_repository.create_movie(title, director, rating)

    return redirect('/movies')


@app.route('/movies/search', methods=['GET', 'POST'])
def search_movies():
    rating = None
    movie_title = None

    if request.method == 'POST':
        movie_title = request.form.get('movie_title', '').strip()

        if movie_title:
            # Use the MovieRepository to get a movie by its title
            movie = movie_repository.get_movie_by_title(movie_title)
            
            if movie:
                rating = movie.rating

    return render_template('search_movies.html', search_active=True, rating=rating, movie_title=movie_title)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    selected_movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', selected_movie=selected_movie, movie_id=movie_id)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)

    if movie is None:
        abort(400)

    movie_repository.delete_movie(movie_id)
    return redirect('/movies')