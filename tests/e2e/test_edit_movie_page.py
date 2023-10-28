from app import movie_repository, redirect, request

def update_movie(movie_id: int):
    
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

    try:
        movie_repository.update_movie(movie_id, title, director, rating)
    except ValueError as e:
        return str(e), 404

    return redirect(f'/movies/{movie_id}')