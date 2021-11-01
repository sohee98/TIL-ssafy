import json


def dec_movies(movies):
    lst = []
    for i in range(len(movies)):
        id = movies[i]['id']
        moviesid_json = open(f'data/movies/{id}.json', encoding='UTF8')
        movies_id = json.load(moviesid_json)
        if movies_id['release_date'][5:7] == '12':
            t = movies_id['title']
            lst.append(t)        
    return lst  
   

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))