# author = 'Daniele Mondello'
# webs   = www.danielemondello.it
# email  = info@danielemondello.it

# import class media where i define attributes of media
import media

# import class fresh_tomatoes where i generate the html
import fresh_tomatoes

# Objects of Movie
# (Title, plot, url_poster, director, genre, year, vote, url_imdb, url_trailer)

Forrest_Gump = media.Movie(
    "Forrest Gump",
    "Forrest Gump, while not intelligent, has accidentally "
    "been present at many historic "
    "moments, but his true love, Jenny Curran, eludes him.",
    "https://www.movieposter.com/posters/archive/main/70/MPW-35447",
    "Robert Zemeckis",
    "Drama",
    "1994",
    "5",
    "http://www.imdb.com/title/tt0109830/?ref_=fn_al_tt_2",
    "https://www.youtube.com/watch?v=uPIEn0M8su0")

Hair = media.Movie(
    "Hair",
    "Claude leaves the family ranch in Oklahoma for New York"
    " where he is rapidly indoctrinated into the "
    "outh subculture and subsequently drafted.",
    "http://curiosando708090.altervista.org/wp-content/"
    "uploads/2012/08/hair.jpg",
    "Milos Forman",
    "Musical",
    "1979",
    "4",
    "http://www.imdb.com/title/tt0079261/?ref_=fn_al_tt_1",
    "https://youtu.be/tC0FRKPuZM4")

Apollo_13 = media.Movie(
    "Apollo 13",
    "NASA must devise a strategy to return Apollo 13 "
    "to Earth safely after the spacecraft undergoes"
    " massive internal damage ",
    "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
    "Ron Howard",
    "Drama",
    "1995",
    "5",
    "http://www.imdb.com/title/tt0112384/?ref_=fn_al_tt_1",
    "https://www.youtube.com/watch?v=Y_rkXC9HH9k")

Back_to_the_future = media.Movie(
    "Back to the Future",
    "A young man is accidentally sent 30 years into the "
    "past in a time-traveling DeLorean "
    "invented by his friend, Dr. Emmett Brown.",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
    "Robert Zemeckis",
    "Adventure",
    "1985",
    "5",
    "http://www.imdb.com/title/tt0088763/?ref_=nv_sr_2",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

Pulp_Fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hit men, a boxer, a gangster's wife, "
    "and a pair of diner bandits intertwine in four tales of "
    "violence and redemption.",
    "http://ia.media-imdb.com/images/"
    "M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4"
    "._V1_SY317_CR4,0,214,317_AL_.jpg",
    "Quentin Tarantino",
    "Crime",
    "1994",
    "5",
    "http://www.imdb.com/title/tt0110912/?ref_=fn_al_tt_1",
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

Alien = media.Movie(
    "Alien",
    "The vessel Nostromo receives a distress call from an planet. "
    "After searching for survivors, the crew heads realize that a deadly "
    "bioform has joined them.",
    "http://ia.media-imdb.com/images/"
    "M/MV5BMTU1ODQ4NjQyOV5BMl5BanBnXkFtZTgwOTQ3NDU2MTE@._V1_SX214_AL_.jpg",
    "Ridley Scott",
    "Sci-FI",
    "1979",
    "4",
    "http://www.imdb.com/title/tt0078748/?ref_=fn_al_tt_1",
    "https://www.youtube.com/watch?v=DGAHtWV7Ua8")

# I create an array with list of movies
movies = [
    Forrest_Gump, Hair, Apollo_13, Back_to_the_future, Pulp_Fiction, Alien]

# Call function open_movies_page from fresh_toematoes and pass array movies
fresh_tomatoes.open_movies_page(movies)

