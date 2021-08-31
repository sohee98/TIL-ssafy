### 1. MTV 

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며, 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오. 

* MTV = Model Template View

* | MVC        | MTV      | 역할                                                         |
  | ---------- | -------- | ------------------------------------------------------------ |
  | Model      | Model    | 데이터 구조를 정의하고 데이터베이스의 기록을 관리            |
  | View       | Template | 파일의 구조나 레이아웃 정의. 실제 내용을 보여주는 데 사용    |
  | Controller | View     | HTTP요청을 수신하고 HTTP응답을 반환.<br />Model을 통해 요청을 충족시키는데 필요한 데이터에 접근. <br />template에게 응답의 서식 설정을 맡김 |

  

### 2. URL 

__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. __(a)__는 무엇인지 작성하시오.

* Variable Routing



### 3. Django template path 

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을 작성하시오.

* templates



## ❖ Django Template Language

1) menus 리스트를 반복문으로 출력하시오

   ```html
   {% for menu in menus %}
       <li>{{ menu }}</li>
   {% endfor %}
   ```

2) posts 리스트를 반복문을 활용하여 0번 글부터 출력하시오.

   ```html
   {% for post in posts %}
       <p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
   {% endfor %}
   ```

3) users 리스트가 비어있다면 **현재 가입한 유저가 없습니다.** 텍스트를 출력하시오.

   ```html
   {% for user in users %}
       <p>{{ user }}</p>
   {% empty %}
       <p>현재 가입한 유저가 없습니다.</p>
   {% endfor %}
   ```


4. 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

   ```html
   {% if forloop.first %}
       <p>첫 번째 반복문 입니다.</p>
   {% else %}
       <p>첫 번째 반복문이 아닙니다.</p>
   {% endif %}
   ```

5. 출력된 결과가 주석과 같아지도록 하시오

   ```<p>{{ menu }}</p>
   <!-- 5 -->
   <p>{{ 'hello'|length }}</p>
   <!-- My Name Is Tom -->
   <p>{{ 'my name is tom'|title }}</p>
   ```

6. 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 작성하시오.

   ```html
   <!-- 2020년 02월 02일 (Sun) PM 02:02 -->
   <p>{{ today|date:"Y년 m월 d일 (D) A h:i" }}</p>
   ```



## Form tag with Django

1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오. 
   * submit이 되면 입력 데이터가 해당 url로 전송된다.
2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.
   * GET, POST, PUT, DELETE ...
3) input 태그에 각각 `안녕하세요`, `반갑습니다`, `파이팅` 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로를 작성하시오.
   * /create/로 이동한다.

