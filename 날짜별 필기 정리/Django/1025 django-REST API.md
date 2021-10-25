# Django 06 - REST API

## [1] HTTP

 <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025110142627.png" alt="image-20211025110142627" style="zoom:67%;" />

<img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025110214844.png" alt="image-20211025110214844" style="zoom:80%;" />



* HTTP request methods
  * 자원에 대한 행위(수행하고자 하는 동작)을 정의
  * 주어진 리소스에 수행하길 원하는 행동을 나타냄
  * GET, POST, PUT, DELETE
* HTTP response status code
  * 요청이 성공적으로 완료되었는지 여부
  * Infomational (1xx), Successful (2xx), Redirection (3xx), Client error (4xx), Server error (5xx) responses

* 웹에서의 리소스 식별
  * HTTP 요청의 대상 = 리소스 (자원) : 문서, 사진, 어떤 것이든 될 수 있음
  * 리소스 식별을 위해 URI로 식별됨

 <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025110607586.png" alt="image-20211025110607586" style="zoom:67%;" />

### URI

 <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025110627995.png" alt="image-20211025110627995" style="zoom: 67%;" />

* 구조

  <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111124652.png" alt="image-20211025111124652" style="zoom: 67%;" />

  * Scheme (protocol) : 브라우저가 사용해야 하는 프로토콜
    * http(s), data, file, ftp, malito
  * Host (Domain name) : 요청을 받는 웹 서버의 이름, IP주소 직접 사용할 수 있음(자주x)
  * Port : 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 '문(gate)' 
    * HTTP 프로토콜의 표준 포트 : HTTP 80, HTTP 443
  * Path : 웹 서버 상의 리소스 경로, 초기-물리적위치, 오늘날-추상화 형태의 구조
  * Query (Identifier) : 웹 서버에 제공되는 추가적인 매개변수, &로 구분되는 key-value 목록
  * Fragment : 자원 안에서의 북마크의 한 종류. 브라우저에게 해당 문서의 특정 부분을 보여주기 위한 방법
    * 브라우저에게 알려주는 요소 - fragment identifier(부분 식별자)라고 부르며, #뒤의 부분은 요청이 서버에 보내지지 않음





## [2] RESTful API

* API

   <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111209827.png" alt="image-20211025111209827" style="zoom:67%;" />

  

* REST

   <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111241211.png" alt="image-20211025111241211" style="zoom:67%;" />

   <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111316875.png" alt="image-20211025111316875" style="zoom:67%;" />

   <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111415922.png" alt="image-20211025111415922" style="zoom:67%;" />



* JSON

   <img src="C:/Users/sohee/AppData/Roaming/Typora/typora-user-images/image-20211025111331971.png" alt="image-20211025111331971" style="zoom:67%;" />



* RESTful API
  * REST 원리를 따라 설계한 API
  * RESTful services, 혹은 simply REST services 라고도 부름
  * 프로그래밍을 통해 클라이언트의 요청에 JSON을 응답하는 서버를 구성
    * 지금까지 사용자의 입장에서 썼던 API를 제공자의 입장이 되어 개발해보기





## [3] Response

* Create Dummy Data

  * django-seed 라이브러리를 사용해 모델 구조에 맞는 데이터 생성

    ```bash
    $ python manage.py seed articles --number=20
    ```

* Response - JsonResponse 

  * JSON-encoded response를 만드는 HttpResponse의 서브 클래스

  * 'safe' parameter : True (기본값)

    * dict 이외의 객체를 직렬화 하려면 False로 설정해야 함

    ```python
    response = JsonResponse({'foo':'bar'})
    response = JsonResponse([1, 2, 3], safe=False)
    ```

  > 직렬화 Serialization : 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정

* Response - Django Serializer

  * HttpResponse를 활용한 JSON 응답 객체

  * 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요가 없음

    <img src="md-images/image-20211025125153582.png" alt="image-20211025125153582" style="zoom:80%;" />

* Response - Django REST Framework

  * Django REST framework(DRF) 라이브러리를 사용한 JSON 응답

    ```bash
    $ pip install djangorestframework	# INSTALLED_APPS에 추가
    ```

  * Model - Article 모델에 맞춰 자동으로 필드를 생성해 serialize 해주는 ModelSerializer 확인

    <img src="md-images/image-20211025125329740.png" alt="image-20211025125329740" style="zoom:67%;" />

  * Response()를 활용

    ![image-20211025125342292](md-images/image-20211025125342292.png)



*  Django REST Framework (DRF)

  * Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
  * DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

  > Web API : 웹 애플리케이션 개발에서 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세

<img src="md-images/image-20211025125643393.png" alt="image-20211025125643393" style="zoom:67%;" />





## [4] Single Model

* DRF with Single Model
  * 단일 모델의 data를 직렬화하여 JSON으로 변환하는 방법에 대한 학습
  * 단일 모델을 두고 CRUD 로직을 수행 가능하도록 설계
  * API 개발을 위한 핵심 기능을 제공하는 도구 활용
    * DRF built-in form, Postman
* ModelSerializer
  * 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut
    * 모델 정보에 맞춰 자동으로 필드 생성
    * serializer에 대한 유효성 검사기를 자동으로 생성
    * .create() & .update()의 간단한 기본 구현이 포함됨

<img src="md-images/image-20211025131839481.png" alt="image-20211025131839481" style="zoom: 80%;" />

* 'many' argument

   <img src="md-images/image-20211025132022995.png" alt="image-20211025132022995" style="zoom: 67%;" />



* Build RESTful API

  <img src="md-images/image-20211025132235071.png" alt="image-20211025132235071" style="zoom: 67%;" />

* #### 1. GET - Article List

  <img src="md-images/image-20211025132547883.png" alt="image-20211025132547883" style="zoom: 67%;" />

   <img src="md-images/image-20211025132427402.png" alt="image-20211025132427402" style="zoom:67%;" />

* #### GET - Article Detail

   <img src="md-images/image-20211025132510845.png" alt="image-20211025132510845" style="zoom:67%;" />

  <img src="md-images/image-20211025132612043.png" alt="image-20211025132612043" style="zoom: 67%;" />

* #### 3. POST - Create Article

   <img src="md-images/image-20211025132641706.png" alt="image-20211025132641706" style="zoom:67%;" />

  ![image-20211025132709041](md-images/image-20211025132709041.png)

<img src="md-images/image-20211025132720466.png" alt="image-20211025132720466" style="zoom:67%;" />

> http://127.0.0.1:8000/api/v1/articles/



 <img src="md-images/image-20211025132824082.png" alt="image-20211025132824082" style="zoom:67%;" />

​    <img src="md-images/image-20211025132836627.png" alt="image-20211025132836627" style="zoom:67%;" />



* #### 4. DELETE - Delete Article

  <img src="md-images/image-20211025132920851.png" alt="image-20211025132920851" style="zoom:67%;" />

  > http://127.0.0.1:8000/api/v1/articles/1/



* #### 5. PUT - Update Article

  <img src="md-images/image-20211025132944619.png" alt="image-20211025132944619" style="zoom:67%;" />

  * HTTP body에 form-data로 title과 content 수정 데이터 작성
  * http://127.0.0.1:8000/api/v1/articles/1/







## [5] 1:N Relation

