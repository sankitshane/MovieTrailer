#imports
import webbrowser

#Class Anime with show_trailer function
class Anime():
    def __init__(self,anime_tiles,anime_genres,poster_image,trailer_youtube):
        self.title = anime_tiles
        self.genres = anime_genres
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
