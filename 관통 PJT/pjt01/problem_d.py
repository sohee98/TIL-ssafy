import json


def max_revenue(movies):
    m = 0
    for i in range(len(movies)):
        id = movies[i]['id']
        moviesid_json = open(f'data/movies/{id}.json', encoding='UTF8')
        movies_id = json.load(moviesid_json)
        if movies_id['budget'] > m:
            m = movies_id['budget']
            t = movies[i]['title']
    return t

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))