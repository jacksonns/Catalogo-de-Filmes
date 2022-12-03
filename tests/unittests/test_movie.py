import pytest
from src.models.movie import Movie

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
