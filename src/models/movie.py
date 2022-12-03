import requests

class Movie:

    def __init__(self, id, title, synopsis, poster):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster
        self.grade = 0
    
    def add_grade(self, new_grade):
        if new_grade > 5:
            raise Exception
        if self.grade == 0:
            self.grade = new_grade
        else:
            self.grade = (self.grade + new_grade) / 2


def getMovieDetails(id, API_KEY, MOVIE_BASE_URL):
    get_movie_details_url = MOVIE_BASE_URL.format(id, API_KEY)
    movie_details_response = requests.get(get_movie_details_url).json()
    id = movie_details_response.get('id')
    title = movie_details_response.get('original_title')
    overview = movie_details_response.get('overview')
    poster = movie_details_response.get('poster_path')

    return Movie(id, title, overview, poster)


def getMoviesList(movies_url):
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

    return movie_results