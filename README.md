# posta - A dead simple Movie Poster "Now Showing" app for Plex

I wanted a simple "now playing" app that will show the current playing movie on Plex, or pick 5 random movies and cycle through them.

- Posters are cached in the `posters` folder and won't be downloaded if already downloaded
- Plex login credentials should be provided via `.env` file or a Plex token should be provided. Refer to the `.env.example` for more info.
- Not possible without the help of [PlexApi](https://python-plexapi.readthedocs.io/en/latest/index.html)
