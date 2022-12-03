import pytest
import requests_mock
from src.models.movie import Movie
from src.models.movie import getMovieDetails, getMoviesList

@pytest.fixture
def movie():
    movie = Movie('123', 'Movie Title', 'Movie Synopsis', 'path_to_poster')
    return movie

class TestMovie():

    def test_add_first_grade(self, movie):
        movie.add_grade(4)
        assert movie.grade == 4

    def test_add_multiple_grades(self, movie):
        movie.add_grade(5)
        movie.add_grade(4)
        movie.add_grade(4)
        assert movie.grade == 4.25
    
    def test_add_invalid_grade(self, movie):
        with pytest.raises(Exception):
            movie.add_grade(6)

    def test_getMovieDetails_success(self, movie):
        with requests_mock.Mocker() as m:
            m.get("https://api.themoviedb.org/3/movie/"+ movie.id +"?api_key= ", json = {
                'id': '123',
                'original_title': 'Movie Title',
                'overview': 'Movie Synopsis',
                'poster_path': 'path_to_poster'
            })
            returnedMovie = getMovieDetails(movie.id, " ", "https://api.themoviedb.org/3/movie/{}?api_key={}")
            assert movie.id == returnedMovie.id
            assert movie.title == returnedMovie.title
            assert movie.synopsis == returnedMovie.synopsis
            assert movie.poster == returnedMovie.poster

    def test_getMovieDetails_fail(self, movie):
        with requests_mock.Mocker() as m:
            with pytest.raises(Exception):
                m.get("https://api.themoviedb.org/3/movie/"+ movie.id +"?api_key= ", text='Not Found', status_code=404)
                returnedMovie = getMovieDetails(movie.id, " ", "https://api.themoviedb.org/3/movie/{}?api_key={}")
