#### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오. 

* URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. (T - URI는 인터넷의 자원을 식별하는 유일한 주소다. HTTP request methods가 자원에 수행하길 원하는 행동을 나타낸다.)

- HTTP Method는 GET과 POST 두 종류 뿐이다. (F - GET, POST, PUT, DELETE 4종류이다.)

- ‘https://www.fifa.com/worldcup/teams/team/43822/create/’는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.  - F (마지막에 /가 없어야 한다.)

  

#### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

* 200 - 요청 성공 응답. 성공 응답 상태 코드
* 400 - 서버가 클라이언트 오류를 감지해 요청을 처리할 수 없거나, 하지 않는다는 것을 의미
* 401 - 클라이언트 오류 응답. 해당 리소스에 유효한 인증 자격 증명이 없기 때문에 요청이 적용되지 않았음을 나타낸다. 403과 달리 인증이 가능하다
* 403 - 클라이언트 오류 응답. 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것
* 404 - 클라이언트 오류 응답. 서버가 요청받은 리소스를 찾을 수 없다는 것을 의미
* 500 - 서버 에러 응답. 요청을 처리하는 과정에서 서버가 예상치 못한 상황에 놓였다는 것을 의미



#### 3. 아래의 모델을 바탕으로 Serializer를 정의하려 한다. serializers.py 파일에 StudentSerializer를 작성하시오.

```python
class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('name', 'age', 'address',)
```



#### 4. Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

* Serializers를 사용하면 querysets와 모델 인스턴스와 같은 복잡한 데이터를 JSON, XML 등 다른 타입으로 쉽게 렌더링할 수 있는 기본 파이썬 데이터 타입으로 변환할 수 있다. 

