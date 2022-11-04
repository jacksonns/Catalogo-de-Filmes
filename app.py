from flask import Flask
import config
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE

app = Flask(__name__, template_folder='src/templates')
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)
mde = SimpleMDE(app)

import src.router

if __name__ == '__main__':
    app.run()