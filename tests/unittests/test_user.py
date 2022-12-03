import pytest
from src.exceptions.password_exception import InvalidPasswordException
from src.models.user_repo import UserRepo
from src.models.user import User

@pytest.fixture
def user():
    return User(password = "senha123")

class TestUser():

    def test_password_verification(self, user):
        assert user.verify_password('senha123')
    
    def test_init_user_with_password_without_upper_case_character(self):
        with pytest.raises(InvalidPasswordException):
            UserRepo('U123', 'fulano', 'email@email.com', '123fulano@')
    
    def test_init_user_with_password_without_eight_characters(self):
        with pytest.raises(InvalidPasswordException):
            UserRepo('U123', 'fulano', 'email@email.com', '123Ful@')

    def test_init_user_with_password_without_numeric_characters(self):
        with pytest.raises(InvalidPasswordException):
            UserRepo('U123', 'fulano', 'email@email.com', 'Fulano!')

    def test_init_user_with_password_without_alphanumeric_characters(self):
        with pytest.raises(InvalidPasswordException):
            UserRepo('U123', 'fulano', 'email@email.com', '123Fulano')
