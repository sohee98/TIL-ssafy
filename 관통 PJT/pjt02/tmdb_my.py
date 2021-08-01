import requests

class TMDBHelper:
    
    def __init__(self, api_key=None):
        self.api_key = api_key
    
    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = 'http://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'
        for k, v in kwargs.itmes():
            request_url += f'&{k}={v}'

        return request_url
        
    # 제목으로 영화 검색 후, 검색결과에서 id를 return    
    def get_movie_id(self, title):
        request_url = self.get_request_url(method='/search/movie', query=title, region='KR', language='ko')
        # 검색 결과 dict
        data = requests.get(request_url).json()         #pprint(data)
        results = data.get('results')               #(results 없을때)key error를 대비하여 .get 사용
        if results:
            movie_id = results[0]['id']
            return movie_id
        else:
            return None


        
tmdb_helper = TMDBHelper('')
print(tmdb_helper.get_request_url(language='ko', region='KR'))
print(tmdb_helper.get_mobie_id('기생충') 


