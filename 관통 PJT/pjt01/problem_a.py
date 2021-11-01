import json
from pprint import pprint


def movie_info(movie):
    d = {}
    d['id'] = movie['id']
    d['title'] = movie['title']
    d['poster_path'] = movie['poster_path']
    d['vote_average'] = movie['vote_average']
    d['overview'] = movie['overview']
    d['genre_ids'] = movie['genre_ids'] 
    return d


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))