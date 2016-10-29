# Imports
import webbrowser

class Anime():
    """Anime constructur takes 4 arguments, those are the anime_tiles,anime_genres
    anime's poster_image_url and the anime's youtube trailer.
    When ever a instance of class Anime is made __init__ function is called by
    default and sets all the values for that perticular instance."""
    def __init__(self,anime_tiles,anime_genres,poster_image,trailer_youtube):
        self.title = anime_tiles
        self.genres = anime_genres
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    """A function called show_trailer when called opens of the browser to show the video
    link in the URL."""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
