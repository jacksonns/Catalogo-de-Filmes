"""Set Flask config variables."""

FLASK_ENV = 'development'
TESTING = True
#SECRET_KEY = environ.get('SECRET_KEY')
STATIC_FOLDER = 'src/static'
#TEMPLATES_FOLDER = 'src/templates'

MOVIE_API_BASE_URL ="https://api.themoviedb.org/3/movie/{}?api_key={}"
MOVIE_API_KEY = 'af8d804575fad92d693d1775092e6217'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///src/app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# AWS Secrets
#AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
#AWS_KEY_ID = environ.get('AWS_KEY_ID')