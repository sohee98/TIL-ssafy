# Python 기초 프로그래밍

### 1. 저장

#### - 무엇을 저장하는가

* 숫자 - int 정수, float 실수, complex 복소수
* 글자 - string 문자열
* 참/거짓 - boolean(True/False)

#### - 어떻게 저장하는가

1. 변수
2. 리스트 ` dust = [58, 40, 70]`   *> 순서대로 나열*
3. 딕셔너리  `dust = {'영등포구':58, '강남구':40}` *> key, value 조합*



### 2. 조건(if)

```python
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```



### 3. 반복

* while

```python
n = 0
while n<3:
    print('출력')
    n += 1
```

* for

```python
dust = [59, 24, 102]
for i in dust:
    print(i)
```



### 함수

1) Built-in Functions 내장함수

2) Non-built-in functions

* 모듈 : 함수들의 집합, 패키지.

  * 활용 : 함수가 포함된 코드를 불러온다(import) -> 함수를 사용한다.

  * ex) random - random.choice(리스트) : 하나의 요소 선택

     					 - random.sample(리스트, 개수) : 특정 요소의 수를 비복원 추출











