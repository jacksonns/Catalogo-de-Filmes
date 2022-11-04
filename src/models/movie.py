class Movie:

    def __init__(self, id, title, synopsis, poster):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster