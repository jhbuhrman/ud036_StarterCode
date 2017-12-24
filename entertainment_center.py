#!/usr/bin/env python3
"""entertainment_center.py - display a collection of my favourite movies

USAGE:
    python3 entertainment_center.py
"""


import media
import fresh_tomatoes


def main():
    """Display a collection of the author's favourite movies."""

    # Collect the movies in this list
    movies = list()

    ex_machina = media.Movie(
        "Ex Machina",
        ("A talented programmer is challenged to perform a variation of the"
         " turing test to a robot"),
        "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",  # NOQA
        "https://www.youtube.com/watch?v=XYGzRB4Pnq8")
    movies.append(ex_machina)

    the_game = media.Movie(
        "The Game",
        ("A wealthy investment banker is given a mysterious gift:"
         " participation in a game that integrates in strange ways with his"
         " everyday life"),
        "https://upload.wikimedia.org/wikipedia/en/5/53/TheGame_poster323.jpg",
        "https://www.youtube.com/watch?v=9HTJh4lzAjk")
    movies.append(the_game)

    apocalypse_now = media.Movie(
        "Apocalypse Now",
        "A Captain on a secret mission in the Vietnam War",
        "https://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=FTjG-Aux_yQ")
    movies.append(apocalypse_now)

    the_empire_strikes_back = media.Movie(
        "The Empire Strikes Back",
        "The second movie of the original Star Wars trilogy",
        "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # NOQA
        "https://www.youtube.com/watch?v=mrCCSN3LkUI")
    movies.append(the_empire_strikes_back)

    intouchables = media.Movie(
        "Intouchables",
        ("After he becomes a quadriplegic from a paragliding accident, an"
         " aristocrat hires a young man from the projects to be his"
         " caregiver."),
        "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
        "https://www.youtube.com/watch?v=0RqDiYnFxTk")
    movies.append(intouchables)

    jurassic_park = media.Movie(
        "Jurassic Park",
        ("During a preview tour, a theme park suffers a major power breakdown"
         " that allows its cloned dinosaur exhibits to run amok."),
        "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=lc0UehYemQA")
    movies.append(jurassic_park)

    # Now call the provided helper function that does the actual work
    fresh_tomatoes.open_movies_page(movies)

    # function main() ends here


if __name__ == '__main__':
    main()

# file entertainment_center.py ends here
