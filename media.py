class Movie(object):
    """A Movie class that holds a movie's title, poster image url, and trailer url

    Attributes:
        title: movie title
        poster_image_url: poster image url
        trailer_youtube_url: youtube url of the movie trailer
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Inits Movie with movie data"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
