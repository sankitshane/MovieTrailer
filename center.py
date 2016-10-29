import anime
import fresh_tomatoes

naruto = anime.Anime("Naruto","Action fiction, Adventure fiction, Fantasy","http://img01.deviantart.net/22f9/i/2015/103/7/d/naruto_poster_by_youaraja-d8juwxp.jpg","https://www.youtube.com/watch?v=mksl3tYdyK4")
death_note = anime.Anime("Death Note","Thriller,Mystery,Horror,Fantasy","http://assets-cf.gbeye.com/thumbnails/lightbox_100332_1456795786.jpg","https://www.youtube.com/watch?v=HK3lkfhX_XY")
code_geass = anime.Anime("Code Geass","Mecha Anime, Visual novel","https://animexuniverse.files.wordpress.com/2014/09/1797842746.jpg","https://www.youtube.com/watch?v=v-AGjx0N24U")
sword_art = anime.Anime("Sword Art Online","Action fiction, Adventure, Science Fiction","http://vignette2.wikia.nocookie.net/enanimanga/images/2/25/Sword-art-online-poster.jpg/revision/latest?cb=20120716181655","https://www.youtube.com/watch?v=VNxxReVeVDI")
shokugeki = anime.Anime("shokugeki no soma","Action, Food War, Adventure","http://data.asiastarz.com/data/thumbs/full/13916/600/0/0/0/poster-for-shokugeki-no-soma-season-2.jpg","https://www.youtube.com/watch?v=NBWwdXZyPEU")
Pokemon = anime.Anime("Pokemon","Action,Fantasy,Adventure","http://img09.deviantart.net/b8a7/i/2015/108/5/3/pokemon_poster_by_viking011-d77ur7y.jpg","https://www.youtube.com/watch?v=NTJHbpjLpjA")

anime_array = [naruto,death_note,code_geass,sword_art,shokugeki,Pokemon]

fresh_tomatoes.open_movies_page(anime_array)
