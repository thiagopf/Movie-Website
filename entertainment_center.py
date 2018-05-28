import fresh_tomatoes
import media


def get_config_list(file_name):
    """
    Get the contents of the file and split using: ***
    :param file_name: name of the config file which have the contents
    :return: list of contents
    """
    config_file = open(file_name)
    contents_list = []
    for contents in config_file:
        # Creates a list and remove all spaces before and after all strings
        contents_list.append(map(str.strip, contents.split('***')))
    return contents_list


def create_series():
    """
    Creates a tv series page by getting the contents from series_config.csv
    """
    series_list = []
    series_contents = get_config_list("series_config.csv")
    for contents in series_contents:
        series_list.append(media.Series(*contents))
    fresh_tomatoes.create_page(series_list, 'series.html')


def create_movies():
    """
    Creates a movies page by getting the contents from movies_config.csv
    """
    movies_list = []
    movies_contents = get_config_list("movies_config.csv")
    for contents in movies_contents:
        movies_list.append(media.Movie(*contents))
    fresh_tomatoes.create_page(movies_list, 'movies.html')


def start_entertainment():
    """
    Creates two pages: seires and movies
    Opens a movies page on web browser
    """
    create_series()
    create_movies()
    fresh_tomatoes.open_page('movies.html')


start_entertainment()
