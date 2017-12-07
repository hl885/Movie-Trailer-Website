import media
import fresh_tomatoes
import grequests
import requests
from flask import Flask


app = Flask(__name__)


def get_video_id(rs):
    # Same youtube video id in a dictionary
    video_id = {}
    for r in rs:
        r = r.json()
        video_id[r["id"]] = r["results"][0]["key"]
    return video_id


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

    # Retrieve youtube video id asynchrounously
    rs = []
    for result in results:
        rs.append(grequests.get(
            video_id_request_uri_pre % (result["id"], api_key)))
    rs = grequests.map(rs)
    video_id = get_video_id(rs)

    # Create a list of Movie objects
    for result in results:
        release_year = result["release_date"][0:4]
        movies.append(media.Movie(
            title=result["original_title"]+" ("+release_year+")",
            poster_image_url=img_uri+result["poster_path"],  # noqa
            trailer_youtube_url=video_uri+video_id[result["id"]]
        ))

    return movies


def main():
    # Generate movie website and open in browser
    return fresh_tomatoes.open_movies_page(create_movie_list())


@app.route('/', methods=['GET'])
def my_app():
    return main()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
