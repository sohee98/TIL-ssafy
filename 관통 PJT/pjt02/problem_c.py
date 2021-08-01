import requests
from tmdb import TMDBHelper
from pprint import pprint

'''
from operator import itemgetter
newlist = sorted(movie_list, key=itemgetter('name'), reverse=True) 
'''

def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    th = TMDBHelper('7c6377fdbf40d8566d0e591005c3dad5')
    request_url = th.get_request_url()
    data = requests.get(request_url).json()
    result = data['results']

    from operator import itemgetter
    sort_movie = sorted(result, key=itemgetter('vote_average'), reverse=True)
    top5_movie = sort_movie[:5]
    
    return top5_movie


if __name__ == '__main__':
    pprint(ranking())

