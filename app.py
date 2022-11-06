from flask import Flask
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__, template_folder='src/templates')
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
mde = SimpleMDE(app)

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy()
from src.models import user, movie_list
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

import src.router

if __name__ == '__main__':
    app.run()