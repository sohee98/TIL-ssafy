import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    pass
    th = TMDBHelper('7c6377fdbf40d8566d0e591005c3dad5')
    m_id = th.get_movie_id(title)
    request_url = th.get_request_url(method=f'/movie/{m_id}/recommendations',language='ko')
    data = requests.get(request_url).json()
    results = data.get('results')
    if results:
        movie_title = []
        for i in range(len(results)):
            movie = results[i]
            movie_title.append(movie['title'])
        return movie_title
    elif results == []:
        return results
    else:
        return None



if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
