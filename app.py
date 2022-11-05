from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder='src/templates')
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
mde = SimpleMDE(app)

db = SQLAlchemy()
from src.models import user
db.init_app(app)
migrate = Migrate(app, db, render_as_batch=True)

auth = Blueprint('auth',__name__)

import src.router

if __name__ == '__main__':
    app.run()