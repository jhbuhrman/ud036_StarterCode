# python3
"""Media Python module for creating movie objects.

Implements the Movie class.

This code is based on the exercises made during Udacity's
'Make classes: ...'-course.
"""


import webbrowser as _webbrowser   # do not pollute the global namespace


#
# Google coding guideline states that class definitions should explicitely
#      inherit from object
#
# But for code written for python3, this is not recommended practice
#
class Movie:
    """Movie class - store some information attributes to describe a movie.

    Methods:
        show_trailer(): Open the corresponding movie trailer
    """

    def __init__(self,
                 movie_title, movie_storyline, poster_image, trailer_youtube):
        """Create a new Movie object.

        movie_title:            title of the movie
        movie_storyline:        one-line synopsis of the movie
        poster_image:           a URL (string) to poster image of the movie
        trailer_youtube:        a URL (string) to a trailer of the movie
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self, new=0, autoraise=True):
        """Show the movie trailer in your default webbrowser.

        new:                    see `webbrowser.open()` documentation
        autoraise:              see `webbrowser.open()` documentation

        Link to documentation:
        * https://docs.python.org/3.1/library/webbrowser.html#webbrowser.open
        """

        _webbrowser.open(self.trailer_youtube_url, new, autoraise)

    # class Movie ends here

# file media.py ends here
