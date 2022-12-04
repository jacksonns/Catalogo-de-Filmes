import pytest
import requests_mock
from src.models.movie import Movie
from src.models.movie import getMovieDetails, getMoviesList
from src.models.user_repo import UserRepo

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
    
    def test_adding_to_watch_list(self, movie):
        user1 = UserRepo('U123', 'fulano1', 'email1@email.com', '123Fulano@')
        user2 = UserRepo('U321', 'fulano2', 'emai2l@email.com', '321Fulano@')
        user1.add_to_want_to_watch_list(movie)
        user2.add_to_want_to_watch_list(movie)
        assert movie.watchers == 2

    def test_is_movie_popular_false(self, movie):
        assert movie.is_popular() == False
        user1 = UserRepo('U123', 'fulano1', 'email1@email.com', '123Fulano@')
        user1.add_to_want_to_watch_list(movie)
        assert movie.is_popular() == False

    def test_is_movie_popular_true(self, movie):
        user1 = UserRepo('U123', 'fulano1', 'email1@email.com', '123Fulano@')
        user2 = UserRepo('U321', 'fulano2', 'emai2l@email.com', '321Fulano@')
        user1.add_to_want_to_watch_list(movie)
        user2.add_to_want_to_watch_list(movie)
        assert movie.is_popular() == True

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

    def test_getMoviesList_success(self):
        with requests_mock.Mocker() as m:
            m.get("https://api.themoviedb.org/3/search/movie?api_key= &query=test", json = {'results': [
                {
                    'id': '123',
                    'original_title': 'Movie Title',
                    'overview': 'Movie Synopsis',
                    'poster_path': 'path_to_poster'
                },
                {
                    'id': '1233',
                    'original_title': 'Movie Title_',
                    'overview': 'Movie Synopsis_',
                    'poster_path': 'path_to_poster_'
                },
            ]})
            list_of_movies = getMoviesList("https://api.themoviedb.org/3/search/movie?api_key= &query=test")
            assert len(list_of_movies) == 2

    def test_getMoviesList_fail(self):
        with requests_mock.Mocker() as m:
            with pytest.raises(Exception):
                m.get("https://api.themoviedb.org/3/search/movie?api_key= &query=test", text='Not Found', status_code=404)
                list_of_movies = getMoviesList("https://api.themoviedb.org/3/search/movie?api_key= &query=test")
