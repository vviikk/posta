# posta - A dead simple Movie Poster "Now Showing" app for Plex

![image](https://user-images.githubusercontent.com/1991125/172079055-bc06509b-40e2-4cfd-b0f2-ade2868d18d9.png)

![image](https://user-images.githubusercontent.com/1991125/172079105-dbafd1b9-ae00-4dfe-83cd-ff6223ed7a06.png)

I wanted a simple "now playing" app that will show the current playing movie on Plex, or pick 5 random movies and cycle through them.

- Posters are cached in the `posters` folder and won't be downloaded if already downloaded
- Plex login credentials should be provided via `.env` file or a Plex token should be provided. Refer to the `.env.example` for more info.
- Done possible with the help of [PlexApi](https://python-plexapi.readthedocs.io/en/latest/index.html) or [Imdbpy](https://cinemagoer.github.io)
