import json
from pprint import pprint


def movie_info(movies, genres):
    lst = []
    for c in range(len(movies)):
        d = {}
        d['genre_names'] = movies[c]['genre_ids'] 
        d['id'] = movies[c]['id']
        d['overview'] = movies[c]['overview']
        d['poster_path'] = movies[c]['poster_path']
        d['title'] = movies[c]['title']
        d['vote_average'] = movies[c]['vote_average']
        
        for a in range(len(d['genre_names'])):
            for i in genres:
                if i['id'] == d['genre_names'][a]:
                    d['genre_names'][a] = i['name']
        lst.append(d)  
    return print(lst)

        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))