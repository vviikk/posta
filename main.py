from urllib.request import urlopen
import os
import os.path
from imdb import Cinemagoer
from plexapi.myplex import MyPlexAccount, PlexServer

from load_env import load_env

load_env()


base_url = os.getenv("POSTA_BASE_URL")
plex_username = os.getenv("POSTA_PLEX_USERNAME")
plex_password = os.getenv("POSTA_PLEX_PASSWORD")
plex_server_name = os.getenv("POSTA_PLEX_SERVER_NAME")
ia = Cinemagoer()


def read_token_from_file():
    with open("token.txt", "r") as myfile:
        token = " ".join([line.replace("\n", "") for line in myfile.readlines()])
    return token


def write_token_to_file(token):
    text_file = open("token.txt", "w")
    text_file.write(token)
    text_file.close()


def get_server():
    token = read_token_from_file()
    if not token:
        plex_account = MyPlexAccount(plex_username, plex_password)
        server = plex_account.resource(plex_server_name).connect()
        write_token_to_file(server.createToken())
    else:
        server = PlexServer(base_url, token)

    return server


def make_safe_filename(s):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"

    return "".join(safe_char(c) for c in s).rstrip("_") + ".jpg"


def get_poster_url(movie_name):
    poster = ia.search_movie(movie_name)[0]["full-size cover url"]
    return poster


def download_poster_to_movie_name(poster_filename, poster_location):
    output_filename = f"posters/{poster_filename}"

    if not os.path.exists(output_filename):
        poster_file = urlopen(poster_location)
        with open(output_filename, "wb") as output:
            output.write(poster_file.read())


server = get_server()

movies = server.library.section("Movies")

for movie in movies.search():
    movie_name = movie.title
    poster_filename = make_safe_filename(movie_name)
    poster_url = get_poster_url(movie_name)
    download_poster_to_movie_name(poster_filename, poster_url)
