import requests
from tmdb import TMDBHelper

tmdb_helper = TMDBHelper('')
url = tmdb_helper.get_request_url(method='/movie/popular', region='KR', language='ko')
data = requests.get(url).json()
popular_movies = data['results'][0]




