from src.exceptions.password_exception import InvalidPasswordException

class UserRepo():

    def __init__(self, id, username, email, password) :
        self.id = id
        self.username = username
        self.email = email
        self.wantToWatchList = []
        self.watchedList = []
        if (self.validate_password(password)):
            self.password = password
    
    def add_to_want_to_watch_list(self, movie):
        self.wantToWatchList.append(movie)
        movie.watchers += 1
    
    def validate_password(self, password):
        if(password.islower() or (len(password) <= 7) or password.isalpha() or password.isalnum()):
            raise InvalidPasswordException(password)
        return True