from app import app
from flask import render_template, request, redirect, url_for
import requests
from src.models.movie import Movie

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

   #search_movie = request.args.get('movie_query')
   #if search_movie:
      #return redirect(url_for('.search',movie_name=search_movie))
   #else:      
   return render_template('home.html',
                           popular = movie_results)