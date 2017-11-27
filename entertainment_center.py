import media
import fresh_tomatoes


def create_movie_list():
    movies = []

    # Create a list of Movie objects
    movies.append(media.Movie(
        title=r"The Shawshank Redemption (1994)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=6hB3S9bIaco"
    ))
    movies.append(media.Movie(
        title=r"The Godfather (1972)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=et2Q96qqd1U"
    ))
    movies.append(media.Movie(
        title=r"The Godfather: Part II (1974)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BMjZiNzIxNTQtNDc5Zi00YWY1LThkMTctMDgzYjY4YjI1YmQyL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,702,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=8PyZCU2vpi8"
    ))
    movies.append(media.Movie(
        title=r"The Dark Knight (2008)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=EXeTwQWrcwY"
    ))
    movies.append(media.Movie(
        title=r"12 Angry Men (1957)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,649,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=Dosg0p7LAB4"
    ))
    movies.append(media.Movie(
        title=r"Schindler's List (1993)",
        poster_image_url=r"https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # noqa
        trailer_youtube_url=r"https://www.youtube.com/watch?v=gG22XNhtnoY"
    ))

    return movies


def main():
    # Generate movie website and open in browser
    fresh_tomatoes.open_movies_page(create_movie_list())


if __name__ == '__main__':
    main()
