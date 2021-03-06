# bot token

* 기본 주소

```
https://api.telegram.org/bot<token>
```

### 요청 URL

`메서드` : 내가 조작할 내용

* 내정보보기

https://api.telegram.org/bot<token>/getMe

* 내정보 업데이트

https://api.telegram.org/bot<token>/getUpdates

* 메시지 보내기

https://api.telegram.org/bot<token>/sendMessage?chat_id=1812985782&text={}



## 실습

#### 1. lotto 모듈 이용하기

* lotto.py 활용하기
  * 모듈화를 하려면 함수로 만들어주기

```python
#로또 번호 6개 추첨 코드 
from random import sample

def get_lotto_num():
    numbers = range(1, 46)
    pick = sorted(sample(numbers, 6))
    return pick
```

- 챗봇 실습
  - `import lotto` 로 [lotto.py](http://lotto.py) 모듈 요청
  - `lotto.get_lotto_num()` 로 로또 번호 부르기

```python
# 요청
import requests
# 내가 만든 lotto.py 요청
import lotto

# 1. 사용자 정보 가져오기
url = f'<https://api.telegram.org/bot<token>/>'

# /getUpdates로 요청 보내서,
url_getup = url + f'getUpdates'
response = requests.get(url_getup).json()

# chat_id에 해당하는 값을 저장
chat_id = response['result'][0]['message']['from']['id']

# 2. 메세지 보내기
# /sendMessage?chat_id={위에서가져온값}&text={원하는 값}

message  = f'오늘의 로또번호는 {lotto.get_lotto_num()} 입니다'
# message = input()
url_send = url + f'sendMessage?chat_id={chat_id}&text={message}'
response_send = requests.get(url_send).json()

# 챗봇에서 확인 가능
```



#### 2. 파파고 코드 이용하기

```python
'''
1. 랜덤 명언을 가져와서 변수에 저장
<https://favqs.com/api/qotd>
'''
import requests

# 0. URL
url = '<https://favqs.com/api/qotd>'
# 1. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
response = requests.get(url).json()
# 2. 해당 내용에서 필요한 부분 꺼내기
print(response['quote']['author'])
quote_body = response['quote']['body']
'''
2. 해당 명언의 내용을 네이버 API를 통해서
papago 번역 결과를 가져온다.
POST <https://openapi.naver.com/v1/papago/n2mt>
필수 파라미터 : source=en, target=ko, text 
'''
# 0. naver에서 발급받은 ID/secret
headers = {
    'X-Naver-Client-Id': '여러분 아이디',
    'X-Naver-Client-Secret': '여러분 비밀번호'
}
# 0. URL
source = 'en'
target = 'ko'
text = quote_body
data = {
    'source': source,
    'target': target,
    'text': text
}
url = f'<https://openapi.naver.com/v1/papago/n2mt>'
# 1. 요청을 보내서 응답받은 JSON을 파이썬 자료구조로
response = requests.post(url, headers=headers, data=data).json()
# 2. 해당 내용에서 필요한 부분 꺼내기
print(text)
print(response['message']['result']['translatedText'])
```



#### 3. flask 서버 이용하기

> 요청 URL : http://sohee.pythonanywhere.com/

```python
# A very simple Flask Hello World app for you to get started with...
import random
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    pick = random.sample(range(1, 46), 6)
    return f'{pick}'

# 1. /lotto
@app.route('/lotto')
def lotto():
    # 파이썬 코드
    pick = random.sample(range(1, 46), 6)
    # 보여줄 것을 문자열로
    return f'{pick}'

# 응답
# 사용자가 요청 보낼 URL 패턴 만들고
@app.route('/dinner')
# 함수를 만들어서
def dinner():
    # 반환하는 것!
    dinner_box = ['카레', '피자', '동원참치삼각김밥', '마라탕', '핫도그', '제육', '돈까스', '피자', '치킨',  '족발', '라면', '초밥', '삼겹살', '샐러드', '꽃등심은 친구에게']
    menu = random.sample(dinner_box, 2)
    return f'{menu[0]} 먹을래? {menu[1]} 먹을래?'

# 이거 하려면 추가 설정이 필요합니다!
# 주소를 크롬창에 요청한번 보내주세요!

@app.route('/telegram', methods=['POST'])
def telegram():
    TOKEN = '<token>'
    BASE_URL = f'<https://api.telegram.org/bot{TOKEN}>'
    response = request.get_json()
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == '/로또':
        text = random.sample(range(1, 46), 6)
    send_message_url = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}'
    response = requests.get(send_message_url).json()
    return 'hi'
```

- /telegram 으로해서 webhook 쓰실 분들은
  - 주소가 반드시 아래의 형식이여야 합니다.
    - https://api.telegram.org/bot토큰/setWebhook?url=파이썬애니웨어여러분주소/telegram
    - 예시)
      - https://api.telegram.org/bot<token>/setWebhook?url=https://takkim.pythonanywhere.com/telegram
  - 그리고 이 경우에는 getUpdates가 되지 않아, 여러분 매일 알림오게끔 한 코드를 getUpdates 쓰지 않고 숫자로 넣어서 해주셔야 합니다.
    - https://api.telegram.org/bot토큰/deleteWebhook 으로 하셔서 지우시면 다시 getUpdates를 쓰실 수 있어요.
