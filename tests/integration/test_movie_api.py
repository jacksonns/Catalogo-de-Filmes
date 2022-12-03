from app import app
import requests
import pytest

@pytest.fixture
def api_key():
    return app.config["MOVIE_API_KEY"]

@pytest.fixture
def movie_url():
    return app.config["MOVIE_API_BASE_URL"]

class TestMovieAPI():

    def test_get_movie_by_id(self, api_key, movie_url):
        search_movie_url = movie_url.format('663712', api_key)
        movie_response = requests.get(search_movie_url).json()
        assert movie_response.get('id') == 663712
        assert movie_response.get('original_title') == 'Terrifier 2'
    
    def test_get_movie_list(self, api_key, movie_url):
        movie_list_url = movie_url.format('popular', api_key)
        movies_response = requests.get(movie_list_url).json()
        assert type(movies_response['results']) == list