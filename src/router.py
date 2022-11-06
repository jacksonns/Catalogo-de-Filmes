from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
import requests
from src.models.movie import Movie
from src.models.user import User
from src.models.review import Review
from src.forms.login_form import LoginForm
from src.forms.registration_form import RegistrationForm
from src.forms.review_form import ReviewForm


MOVIE_BASE_URL = app.config["MOVIE_API_BASE_URL"]
API_KEY = app.config["MOVIE_API_KEY"]


@app.route('/')
def home():
    movies_url = MOVIE_BASE_URL.format("popular", API_KEY)
    movies_response = requests.get(movies_url).json()

    movie_results = []
    if movies_response['results']:
        movie_results_list = movies_response['results']

        for movie_item in movie_results_list:
            id = movie_item.get('id')
            title = movie_item.get('original_title')
            overview = movie_item.get('overview')
            poster = movie_item.get('poster_path')

            if poster:
                movie_object = Movie(id, title, overview, poster)
                movie_results.append(movie_object)

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('.search', movie_name=search_movie))
    else:
        return render_template('home.html', popular=movie_results)


@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(API_KEY, movie_name)
    search_movie_response = requests.get(search_movie_url).json()

    search_movie_results = []

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        movie_results = []
        for movie_item in search_movie_list:
            id = movie_item.get('id')
            title = movie_item.get('original_title')
            overview = movie_item.get('overview')
            poster = movie_item.get('poster_path')

            if poster:
                movie_object = Movie(id, title, overview, poster)
                movie_results.append(movie_object)
        search_movie_results = movie_results

    title = f'search results for {movie_name}'
    return render_template('search.html',
                           title=title,
                           movies=search_movie_results)


@app.route("/movie/<int:id>")
def movie(id):
    get_movie_details_url = MOVIE_BASE_URL.format(id, API_KEY)
    movie_details_response = requests.get(get_movie_details_url).json()

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')

        movie_object = Movie(id, title, overview, poster)

    movie = movie_object
    title = f'{movie.title}'
    reviews = Review.query.filter_by(movie_id = id).all()
    return render_template('movie.html',
                           id=id,
                           title=title,
                           movie=movie,
                           reviews = reviews)


@app.route("/watched/<int:id>")
@login_required
def watched(id):
    user = current_user
    if user.watchedList is None:
        flash("Filme inserido com sucesso!")
        user.watchedList = [id]
    else:
        if id not in user.watchedList:
            watchedList = user.watchedList
            watchedList.append(id)
            user.watchedList = watchedList
            flash("Filme inserido com sucesso!")
        else:
            flash("Filme já inserido!")

    db.session.commit()
    return redirect(url_for("home"))


@app.route("/towatch/<int:id>")
@login_required
def to_watch(id):
    user = current_user
    if user.wantToWatchList is None:
        flash("Filme inserido com sucesso!")
        user.wantToWatchList = [id]
    else:
        if id not in user.wantToWatchList:
            wantToWatchList = user.wantToWatchList
            wantToWatchList.append(id)
            user.wantToWatchList = wantToWatchList
            flash("Filme inserido com sucesso!")
        else:
            flash("Filme já inserido!")

    db.session.commit()
    return redirect(url_for("home"))


def my_list():
    user = current_user
    wantToWatchList = []
    for movie in user.wantToWatchList:
        get_movie_details_url = MOVIE_BASE_URL.format(movie, API_KEY)
        movie_details_response = requests.get(get_movie_details_url).json()

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')

            movie_object = Movie(id, title, overview, poster)

        wantToWatchList.append(movie_object)

    watchedList = []
    for movie in user.watchedList:
        get_movie_details_url = MOVIE_BASE_URL.format(movie, API_KEY)
        movie_details_response = requests.get(get_movie_details_url).json()

        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')

            movie_object = Movie(id, title, overview, poster)

        watchedList.append(movie_object)


''' Authentication '''


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("home"))

        flash("E-mail ou senha inválidos")

    title = "Login"
    return render_template("login.html",
                           login_form=login_form,
                           title=title)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    title = "Nova Conta"
    return render_template("register.html",
                           registration_form=form,
                           title=title)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/profile")
def profile():
    return "User Profile"


@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()

    get_movie_details_url = MOVIE_BASE_URL.format(id, API_KEY)
    movie_details_response = requests.get(get_movie_details_url).json()

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')

        movie_object = Movie(id, title, overview, poster)

    movie = movie_object

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie_id = movie.id,
                            movie_title = movie.title,
                            image_path = movie.poster,
                            review_title = title,
                            movie_review = review,
                            user_id = current_user.id)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',
                            title = title, 
                            review_form = form, 
                            movie = movie)


@app.route('/review')
def open_review():
    return "Review details"