from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE

app = Flask(__name__)
bootstrap = Bootstrap(app)
mde = SimpleMDE(app)


@app.route('/')
@app.route('/home')
def home():
   return render_template("base.html")

if __name__ == '__main__':
    app.run()