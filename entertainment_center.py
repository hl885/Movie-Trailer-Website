import media
import fresh_tomatoes
import requests


def get_video_id(url):
    # Retrieve youtube video id
    payload = "{}"
    response = requests.request("GET", url, data=payload)
    results = response.json()["results"]
    return results[0]["key"]


def create_movie_list():
    movies = []

    # Define tmdb api key and neccesary request URI
    api_key = input('tmdb API key: ')
    img_uri = "https://image.tmdb.org/t/p/w640"  # noqa
    video_uri = "https://www.youtube.com/watch?v="  # noqa
    video_id_request_uri_pre = "https://api.themoviedb.org/3/movie/%s/videos?api_key=%s&language=en-US"  # noqa
    movie_request_uri_pre = "https://api.themoviedb.org/3/movie/popular?api_key=%s&language=en-US&page=1"  # noqa
    movie_request_uri = movie_request_uri_pre % api_key

    # Retrieve popular movies from tmdb api
    payload = "{}"
    response = requests.request("GET", movie_request_uri, data=payload)
    results = response.json()["results"]

    # Create a list of Movie objects
    for result in results:
        video_id_request_uri = video_id_request_uri_pre % (
            result["id"], api_key)
        video_id = get_video_id(video_id_request_uri)
        release_year = result["release_date"][0:4]
        movies.append(media.Movie(
            title=result["original_title"]+" ("+release_year+")",
            poster_image_url=img_uri+result["poster_path"],  # noqa
            trailer_youtube_url=video_uri+video_id
        ))

    return movies


def main():
    # Generate movie website and open in browser
    fresh_tomatoes.open_movies_page(create_movie_list())


if __name__ == '__main__':
    main()
