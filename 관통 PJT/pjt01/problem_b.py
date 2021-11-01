import json
from pprint import pprint


def movie_info(movie, genres):
    d = {}
    d['id'] = movie['id']
    d['title'] = movie['title']
    d['poster_path'] = movie['poster_path']
    d['vote_average'] = movie['vote_average']
    d['overview'] = movie['overview']
    d['genre_names'] = movie['genre_ids'] 
    for a in range(len(d['genre_names'])):
        for i in genres:
            if i['id'] == d['genre_names'][a]:
                d['genre_names'][a] = i['name']
    return d  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))