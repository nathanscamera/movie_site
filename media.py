#import web browser to open the youtube trailer link in a new window

import webbrowser

#The movie class holds all the attributes we want to use

class Movie( ):
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube, one_word):  # noqa
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.word = one_word

#Opens web browser

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
