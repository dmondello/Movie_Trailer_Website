# author = 'Daniele Mondello'
# webs   = www.danielemondello.it
# email  = info@danielemondello.it

# import the module webbrowser
import webbrowser


# Create class Movie
class Movie:
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 movie_director, movie_genre, movie_year, movie_vote,
                 movie_imdb, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.director = movie_director
        self.genre = movie_genre
        self.year = movie_year
        self.vote = movie_vote
        self.imdb = movie_imdb
        self.trailer_youtube_url = trailer_youtube_url

# Define function show_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
