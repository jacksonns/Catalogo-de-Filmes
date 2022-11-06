import requests


class Movie:

    def __init__(self, id, title, synopsis, poster):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster


def getMovieDetails(id, API_KEY, MOVIE_BASE_URL):
    get_movie_details_url = MOVIE_BASE_URL.format(id, API_KEY)
    movie_details_response = requests.get(get_movie_details_url).json()

    id = movie_details_response.get('id')
    title = movie_details_response.get('original_title')
    overview = movie_details_response.get('overview')
    poster = movie_details_response.get('poster_path')

    return Movie(id, title, overview, poster)
