class InvalidPasswordException(Exception):
    def __init__(self, password):
        if password.islower():
            message = "Password must have at least one upper case character."
        elif (len(password) <= 7) :
            message = "Password must be at least 8 characters long."
        elif password.isalpha() :
            message = "Password requires at least one number."
        elif password.isalnum() :
            message = "Password requires at least one special character."
        super().__init__(message)