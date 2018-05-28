import webbrowser


class Movie:

    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        """
        Store the arguments
        :param movie_title: a string containing the title of the movie
        :param storyline: a string containing the storyline of the movie
        :param poster_image: a string containing the url of the poster image
        :param trailer_youtube: a string containing the url of the youtube trailer
        """
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens a web browser by using the youtube url
        """
        webbrowser.open(self.trailer_youtube_url)


class Series(Movie):
    def __init__(self, movie_title, storyline, poster_image, trailer_youtube, number_of_seasons):
        """
        Store the arguments
        :param movie_title: a string containing the title of the movie
        :param storyline: a string containing the storyline of the movie
        :param poster_image: a string containing the url of the poster image
        :param trailer_youtube: a string containing the url of the youtube trailer
        :param number_of_seasons: a string containing the number of seasons
        """
        Movie.__init__(self, movie_title, storyline, poster_image, trailer_youtube)
        self.number_of_seasons = number_of_seasons
