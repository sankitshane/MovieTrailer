# MovieTrailer

It is a simple Movie trailer web application that uses python as the data structure
and as a backend part of the program.

### Run the code
Just run the center.py code and a browser window will pop up with all the info.

### Work flow
center.py contains all the data. It will create instances of class Anime and put it
in a array called anime_array.

Then anime_array is passed as a argument to open_movies_page function in fresh_tomatoes.py
which creates the content with create_movie_tiles_content function and renders it in the
browser.
