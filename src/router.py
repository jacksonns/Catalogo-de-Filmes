from app import app
from flask import render_template, request, redirect, url_for
import requests
from src.models.movie import Movie

MOVIE_BASE_URL = app.config["MOVIE_API_BASE_URL"]
API_KEY = app.config["MOVIE_API_KEY"]


@app.route('/')
def home():
    movies_url = MOVIE_BASE_URL.format("popular", API_KEY)
    movies_response = requests.get(movies_url).json()

    movie_results = []
    if movies_response['results']:
        movie_results_list = movies_response['results']

        for movie_item in movie_results_list:
            id = movie_item.get('id')
            title = movie_item.get('original_title')
            overview = movie_item.get('overview')
            poster = movie_item.get('poster_path')

            if poster:
                movie_object = Movie(id, title, overview, poster)
                movie_results.append(movie_object)

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('home.html', popular=movie_results)


@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(API_KEY, movie_name)
    search_movie_response = requests.get(search_movie_url).json()

    search_movie_results = []

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        movie_results = []
        for movie_item in search_movie_list:
            id = movie_item.get('id')
            title = movie_item.get('original_title')
            overview = movie_item.get('overview')
            poster = movie_item.get('poster_path')

            if poster:
                movie_object = Movie(id, title, overview, poster)
                movie_results.append(movie_object)
        search_movie_results = movie_results

    title = f'search results for {movie_name}'
    return render_template('search.html',
                           title=title,
                           movies=search_movie_results)


@app.route("/movie/<int:id>")
def movie(id):
    get_movie_details_url = MOVIE_BASE_URL.format(id, API_KEY)
    movie_details_response = requests.get(get_movie_details_url).json()

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')

        movie_object = Movie(id, title, overview, poster)

    movie = movie_object
    title = f'{movie.title}'
    return render_template('movie.html',
                           id=id,
                           title=title,
                           movie=movie)
