from flask import Flask, render_template, send_from_directory
import random
from urllib.request import urlopen
import os
import os.path
from imdb import Cinemagoer
from plexapi.myplex import MyPlexAccount, PlexServer

from load_env import load_env

load_env()


base_url = os.getenv("POSTA_PLEX_BASE_URL")
plex_username = os.getenv("POSTA_PLEX_USERNAME")
plex_password = os.getenv("POSTA_PLEX_PASSWORD")
plex_server_name = os.getenv("POSTA_PLEX_SERVER_NAME")
plex_movie_library = os.getenv("POSTA_PLEX_MOVIE_LIBRARY")
plex_token = os.getenv("POSTA_PLEX_TOKEN")
header_text_now_playing = os.getenv("POSTA_TEXT_NOW_PLAYING", "NOW PLAYING")
header_text_idle = os.getenv("POSTA_TEXT_IDLE", "COMING SOON")
ia = Cinemagoer()


def get_server():
    if not plex_token:
        plex_account = MyPlexAccount(plex_username, plex_password)
        server = plex_account.resource(plex_server_name).connect()
    else:
        server = PlexServer(base_url, plex_token)

    return server


def make_safe_filename(s, y):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"

    return "".join(safe_char(c) for c in s).rstrip("_") + f"_{y}.jpg"


def get_poster_url(movie_name):
    poster = ia.search_movie(movie_name)[0]["full-size cover url"]
    return poster


def get_poster_file_name(movie):
    movie_name = movie.title
    movie_year = movie.year
    return make_safe_filename(movie_name, movie_year)


def download_poster_to_movie_name(movie):
    poster_filename = get_poster_file_name(movie)
    output_filename = f"posters/{poster_filename}"

    if not os.path.exists(output_filename):
        poster_location = get_poster_url(movie.title)
        poster_file = urlopen(poster_location)
        with open(output_filename, "wb") as output:
            output.write(poster_file.read())
            print(f"Poster downloaded: {movie.title} ({movie.year})")
    else:
        print(f"Poster already downloaded: {movie.title} ({movie.year})")


app = Flask(__name__, static_url_path="/static")

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posters")


@app.route("/posters/<path:path>", methods=["GET"])
def static_proxy(path):
    return send_from_directory(root, path)


@app.route("/")
def show_posters():
    server = get_server()

    current_sessions = [
        session for session in server.sessions() if session.type == "movie"
    ]
    now_playing = False

    if len(current_sessions):
        now_playing = True

    movies = server.library.section(plex_movie_library).search()

    random_movies = random.sample(movies, 5)

    for movie in random_movies:
        print(f"Analyzing {movie.title} ({movie.year})")

        download_poster_to_movie_name(movie)

    if not now_playing:
        posters = [get_poster_file_name(movie) for movie in random_movies]
    else:
        posters = [get_poster_file_name(movie) for movie in current_sessions]

    return render_template(
        "index.html",
        heading=header_text_now_playing if now_playing else header_text_idle,
        movie_posters=posters,
    )


if __name__ == "__main__":
    app.run(debug=True)
