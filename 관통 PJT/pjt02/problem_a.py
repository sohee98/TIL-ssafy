import requests
from tmdb import TMDBHelper
# api_key = '7c6377fdbf40d8566d0e591005c3dad5'

def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    tmdb_helper = TMDBHelper('7c6377fdbf40d8566d0e591005c3dad5')
    
    request_url = tmdb_helper.get_request_url()
    data = requests.get(request_url).json()
    result = data['results']
    return len(result)




if __name__ == '__main__':
    print(popular_count())
