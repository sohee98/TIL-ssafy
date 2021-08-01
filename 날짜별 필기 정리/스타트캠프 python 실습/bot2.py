import random
import requests
'''
1. 사용자 정보 가져오기
base_url/getUpdates로 요청 보내서,
chat_id에 해당하는 값을 저장
'''
# 0. 정보 
TOKEN = '1867056710:AAFnhePR2RntFlugrCtQXUFl0JRF82BnuVc'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
# 1. url 요청하고, 결과를 python 자료구조로 저장
get_updates_url = f'{BASE_URL}/getUpdates'
response = requests.get(get_updates_url).json()
chat_id = response['result'][0]['message']['chat']['id']
'''
# 2. 메시지 보내기
# base_url/sendMessage?chat_id={위에서가져온값}&text={원하는 값}
# 메시지 보내기
'''
# 0. 메시지 준비
magic_number = random.sample(range(1, 46), 6)
text = f'''
오늘의 로또 번호 : {magic_number}'''

# 1. 요청
send_message_url = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={text}'
response = requests.get(send_message_url).json()
print(f'메시지 보낸 결과 : {response["ok"]}')


# def sendmessage(x):
#     send_message_url = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={x}'
#     requests.get(send_message_url)
# sendmessage('뭐해')


url = 'https://www.metaweather.com/api/location/1132599'
response = requests.get(url)
result = response.json()
day = result['consolidated_weather'][0]

trans = {
    'Snow': '눈',
    'Sleet' : '진눈깨비',
    'Hail' : '우박',
    'Thunderstorm' : '뇌우',
    'Heavy Rain' : '폭우',
    'Light Rain' : '가벼운 비',
    'Showers' : '소나기',
    'Heavy Cloud' : '구름많음',
    'Light Cloud' : '구름조금',
    'Clear' : '맑은'
}
weather = ''
for day in result['consolidated_weather']:
    weather += f'''{day['applicable_date']} : {trans[day["weather_state_name"]]}
최고기온은 {day["max_temp"]:2.2}, 최저기온은 {day["min_temp"]:2.2}'''


send_message_url2 = f'{BASE_URL}/sendMessage?chat_id={chat_id}&text={weather}'
response = requests.get(send_message_url2).json()

