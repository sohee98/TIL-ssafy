import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    th = TMDBHelper('7c6377fdbf40d8566d0e591005c3dad5')
    m_id = th.get_movie_id(title)
    request_url = th.get_request_url(method=f'/movie/{m_id}/credits')
    data = requests.get(request_url).json()

    if data.get('cast') and data.get('crew'):
        new_cast = []
        for i in range(len(data['cast'])):
            if data['cast'][i]['cast_id'] < 10:
                new_cast.append(data['cast'][i]['name'])
        new_crew = []
        for i in range(len(data['crew'])):
            if data['crew'][i]['department'] == 'Directing':
                new_crew.append(data['crew'][i]['name'])
        new_dict = {'cast':new_cast, 'crew':new_crew}
        return new_dict
        
    else:
        return None
    
    




if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))
