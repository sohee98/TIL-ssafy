# 0. import!
# 항상 최상단에 작성을 해주세요.
import requests

# 1. URL에 파이썬으로 요청
url = 'https://www.metaweather.com/api/location/1132599'
response = requests.get(url)
# 2. JSON 형식을 파이썬 자료구조 변환 (.json())
result = response.json()
# 3. 원하는 값을 추출
# print(result['consolidated_weather'])
# print(type(result['consolidated_weather']))
# 4. 첫번째 데이터
day = result['consolidated_weather'][0]

print(f'''{day['applicable_date']} : {day["weather_state_name"]}
최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}''')

# 5. 무엇을 반복해야하는가?
# result['consolidated_weather']!!!
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
for day in result['consolidated_weather']:
    print(f'''{day['applicable_date']} : {trans[day["weather_state_name"]]}
최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}''')