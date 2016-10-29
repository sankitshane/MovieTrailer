import webbrowser

class Movies():
    def __init__(self,movie_tiles,movie_storyline,poster_image,trailer_youtube):
        self.tiles = movie_tiles
        self.storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
