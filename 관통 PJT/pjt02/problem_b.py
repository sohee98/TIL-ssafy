import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    th = TMDBHelper('7c6377fdbf40d8566d0e591005c3dad5')
    
    request_url = th.get_request_url(language='ko')
    data = requests.get(request_url).json()
    result = data['results']
    new_movie = []
    for i in range(len(result)):
        if result[i]['vote_average'] >= 8:
            new_movie.append(result[i])
    return new_movie

    


if __name__ == '__main__':
    pprint(vote_average_movies())
