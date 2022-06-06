# posta - A dead simple Movie Poster "Now Showing" app for Plex

![image](https://user-images.githubusercontent.com/1991125/172078821-6afb7dcb-19cb-40e2-b0fe-255fbcc54a90.png)

I wanted a simple "now playing" app that will show the current playing movie on Plex, or pick 5 random movies and cycle through them.

- Posters are cached in the `posters` folder and won't be downloaded if already downloaded
- Plex login credentials should be provided via `.env` file or a Plex token should be provided. Refer to the `.env.example` for more info.
- Not possible without the help of [PlexApi](https://python-plexapi.readthedocs.io/en/latest/index.html)
