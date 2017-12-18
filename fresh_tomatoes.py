
# This file is suitable for python3


import webbrowser
import os
import re


# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
MAIN_PAGE_CONTENT = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
MOVIE_TILE_CONTENT = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''

# The (verbose) regex to extract the movie trailer Youtube ID from a URL
YOUTUBE_ID_RE = r'''(v=|be/)      # text to search must be preceded by either
                                  # "v=" or "be/"
                    (?P<trailer_youtube_id>[^&#]+)
                                  # one or more characters, anything other than
                                  # "&" and "#" ...
                                  # accessible under "trailer_youtube_id"'''


def create_movie_tiles_content(movies):
    """Create the HTML content for all movie tiles.

    Parameters:
    movies: an iterable of Movie instances

    each Movie instance should contain at least the following attributes:
    * movie_title: the title of the movie
    * poster_image_url: a URL pointing to movie's the poster image
    * trailer_youtube_url: a URL pointing to the movie's Youtube trailer

    It returns the HTML content displaying the movie tiles.
    """

    regex = re.compile(YOUTUBE_ID_RE, re.VERBOSE)
    # Collect the HTML content in a list of strings
    content = list()
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = regex.search(movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group('trailer_youtube_id')

        # Append the tile for the movie with its content filled in
        content.append(MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id))

    # Now join all the parts together and return it
    return ''.join(content)


def open_movies_page(movies):
    """Create (or overwrite) an html file displaying all the movie tiles.

    It takes a list of Movie instances that serves as input for the rendering.
    See also the description of the create_movie_tiles_content function.
    """
    
    with open('fresh_tomatoes.html', 'w') as output_file:
        # Replace the movie tiles placeholder generated content
        rendered_content = MAIN_PAGE_CONTENT.format(
            movie_tiles=create_movie_tiles_content(movies))
        # Output the file
        output_file.write(MAIN_PAGE_HEAD + rendered_content)

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
