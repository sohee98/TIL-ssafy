### 크롤링

```python
# 0. requests 패1키지를 가져온다.
import requests
from bs4 import BeautifulSoup

# 1. url을 준비한다.
url = 'https://finance.naver.com/sise/'
# 2. 파이썬으로 요청을 보낸 결과를 저장
response = requests.get(url).text
# 3. 정보 추출을 위해서, BeautifulSoup으로 문서 구조화
# -> html으로 구조화
data = BeautifulSoup(response, 'html.parser')
# 4. 선택자를 활용해서 해당 위치를 찾고
kospi = data.select_one('#KOSPI_now')
# 5. 내용을 출력한다.
print(kospi.text)
```

`BeautifulSoup(문서)` : 문서를 보기 좋게 만들기
`.select(selector)` : 특정내용을 뽑아줘
`.select_one(selector)` : 특정내용을 하나만 뽑아줘





### API

> 크롤링 = 비효율적. text로만 출력
>
> API = 보기 편하게 string이 아니라 딕셔너리로 전환해줌
>
> API 키가 필요



``` python 
<url> 
?						#url과 parameter 구분 : ?
api_key=<key>	#필수
&						#parameter과 parameter 구분 : &
language=ko		#옵션
&
region=KR


```

```python
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
        results = data.get('results')  #(results 없을때)key error를 대비하여 .get 사용
        if results:
            movie_id = results[0]['id']
            return movie_id
        else:
            return None


        
tmdb_helper = TMDBHelper('')
print(tmdb_helper.get_request_url(language='ko', region='KR'))
print(tmdb_helper.get_mobie_id('기생충') 
    
```



