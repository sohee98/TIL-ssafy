# 0. requests 패키지를 가져온다.
import requests
from bs4 import BeautifulSoup

# 1. url을 준비한다.
url = 'https://finance.naver.com/sise/'
# 2. 파이썬으로 요청을 보낸 결과를 저장
response = requests.get(url).text
# 3. 정보 추출을 위해서, BeautifulSoup으로 문서 구조화
data = BeautifulSoup(response, 'html.parser')
# 4. 선택자를 활용해서 해당 위치를 찾고
kospi = data.select_one('#KOSPI_now')
# 5. 내용을 출력한다.
print(kospi.text)