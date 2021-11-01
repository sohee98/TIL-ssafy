## A. 프로젝트 만들기

* 가장 먼저 프로젝트를 만든 후, 앱을 만듬
  * `$ django-admin stratproject pjt04`
  *  `$ python manage.py startapp movies `
* pjt04과 movies에 templates 폴더를 만들고 movies에 ulr.py를 만듬
* settings.py > INSTALLED_APPS에 `'movies', 'django_extensions',` 추가
* settings.py > TEMPLATES에  `'DIRS': [BASE_DIR / 'templates'],` 변경

> 프로젝트를 계속 만들다보니 settings.py을 바꾸는 것은 점점 익숙해져갔다. base directory를 설정하고, 앱을 만들때 마다 setting에 추가하는 것은 잘 잊을 수 있지만 하지 않으면 작동을 안하기에 정말 중요하다!



## B. Model

* models.py안에 Movie클래스를 만든 후, 필드명, 타입을 지정해줌
* 생성, 수정시간도 추가
* 제목 쉽게 볼 수 있게 `def __str__(self): return self.title ` 추가
* `$ python manage.py makemigrations `
* `$ python manage.py migrate` 실행함

> 표의 속성들을 추가해줬다. 길이 제한도 둘 수 있고, 생성, 수정시간은 자동으로 추가되게 만들었다. 
>
> model 수정 후,  migrate을 해줘야 하는데 makemigrations만 하고 하지않아서 오류가 났었는데, 원인을 몰라서 한참을 헤맸다. migrate은 정말 중요하고 앞으로는 절대 까먹지 않을 것 같다.



## C. Admin

* admin.py파일 안에 `admin.site.register(Movie)` 추가
* createsuperuser
  * id : user, password : p1p1

> admin user를 추가해서 /admin 에서 파일을 생성, 삭제, 추가할 수 있게 만들었다. 이렇게 관리자 메뉴가 따로 있다는 점이 정말 좋은거 같고 내용 생성, 삭제 등 관리도 할 수 있어 편리하다. 



## D. URL

* pjt04/urls.py 에 include를 써서 movies.urls를 사용하도록 함
* movies/urls.py : app_name을 movies로 함
* `from movies import **views` 추가
* path구문으로 url패턴 만들고 name으로 이름 만듬
  * 전체 영화 목록 조회 : index, 단일 영화 상세 조회 : detail로 만듬

> path를 잘 만드는게 정말 중요하다. 처음에 import를 안하면 오류가 나는데, 처음에 경로설정을 잘 못해서 헷갈렸지만 이제는 어떻게 하는지 알겠다. 그리고 <>안에 int처럼 타입도 꼭 넣어야 하고, name설정도 하는게 좋다. 실수 할 부분이 많아 조심해야 한다.



## E. View & Template

* #### 공유 템플릿 생성 및 사용

* templates/base.html 만듬

  * bootstrap을 이용해서 navbar를 만들고, 색깔을 바꿈
  * navbar에서 Movie와 Home을 누르면 영화 목록 페이지 조회함
  * New를 누르면 새롭게 작성할 수 있는 페이지로 감
  * {% block content %}를 추가

> bootstrap의 기능이 정말 많아 사용할 수록 너무 편리하다. 보기좋은 색깔로 바꾸고, 편리하게 Movie를 눌러도 Home처럼 index로 가게 만들었다. 이렇게 base를 만들어 놓으면 다른 html파일 만들때 navbar도 같이 만들어져서 너무 편리하고 좋다.



* #### 전체 영화 목록 조회

* views.py의 index함수에 `movies = Movie.objects.all()`를 사용하여 모든 목록을 가져옴

* index.html 만듬

  * '영화목록' 이라는 이름과 함께 영화의 제목과 줄거리가 순서대로 나옴
  * {% for %} 사용하여 모든 목록을 출력
  * 영화 제목을 누르면 상세페이지로 가도록 url 설정

> 가장 먼저 보이는 기본 페이지이기 때문에 이쁘게 만들고 싶었지만 꾸밀시간은 부족해서 글씨 두께, 글씨 크기 등 최대한 어울리게 만들었다. html파일에서 오류가 나도 어디에서 오류가 나는지 몰라서 한참 헤맸었다. 처음 적을때 오류가 안나도록 잘 적어야 겠다.



* #### 새로운 영화 작성 Form

* views.py에 new와 create 함수를 만듬
* new로 새로운 데이터를 만들고, create으로 목록에 저장
* navbar의 New로 새롭게 작성 가능
* new.html 만듬
  * {% csrf_token %} 사용
  * 작성칸을 label, input, textarea를 사용하여 만듬
  * 마지막에 작성을 누르면 `url 'movies:create'`로 이동하도록 action 설정, method='POST'로 함
  * 취소 버튼도 만들어 누르면 영화목록페이지로 가도록 만듬

> 함수를 2개를 사용해서 데이터를 만들고 저장하는것을 만들었다. 편리하게 취소버튼도 만들었다. 저장됬을때는 처음 목록페이지로 가도록 해서 만들어진 데이터가 바로 보인다. label과 input, textarea를 잘 사용할 수 있게 id와 name을 잊지않고 적어야되는데 name을 적지 않아서 오류가 났었다. 



* #### 영화 데이터 저장

* create으로 movie의 title, overview, poster_path를 목록에 저장하게 함
* redirect를 사용해서 전체 영화 목록 조회 페이지로 가서 새로고침하게 만듬
* 작성 페이지에서 작성 버튼을 누르면 데이터가 저장되도록 함

> 중요한 점 : 저장을 할 때, `movie.save()` 구문을 꼭 적어야 저장이 된다. redirect를 사용하지 않으면 페이지가 새로고침이 안돼서 링크는 create에 남아있게 된다. 예전에 이렇게 오류가 났어서 이제는 redirect를 언제 사용해야 하는지 알게 됐다.



* #### 단일 영화 상세 조회

* views.py에 detail 함수 만들어 `movie = Movie.objects.get(pk=pk)`사용해서 영화의 번호로 상세 내용을 조회하도록 함

* detail.html을 만듬
  * 영화 제목을 누르면 상세페이지로 와지고, 영화의 상세 정보가 나옴
  * 제목, 줄거리, 포스터 경로 글자의 크기를 다르게 하고 작성시간, 수정시간도 글씨가 옅게 나오게 함
  * 수정, 삭제, 취소 버튼을 만듬

> 영화의 제목, 줄거리, 포스터 경로를 자세히 볼 수 있다. 여기에도 편리하게 취소버튼을 추가했다. 보기 편하게 작성시간, 수정시간은 옅게하고 나머지 글자들의 크기를 다르게 했다. button에 링크를 거는 방법을 잊어버려서, 찾아보면서 만들었다. 버튼의 색깔도 다 다르게 했다.



* #### 수정, 삭제 기능

* views.py에 edit, update, delete 함수를 만듬
* edit으로 데이터를 수정하는 페이지를 띄우고, update로 수정함
* 영화 상세정보에서 수정버튼을 누르면 수정하는 페이지로 감
* edit.html을 만듬
  * new와 똑같이 만들었는데, input에 `value='{{ movie.title }}'`를 추가하고 textarea에도 추가해서 선택한 영화의 정보가 나옴
  * 저장버튼을 누르면 `url: update`로 가서 수정한 정보를 저장하고,  수정한 정보를 보여주기 위해 상세 정보 페이지를 보여줌
* update함수에서 redirect를 사용하여 상세정보 창이 새로고침되도록 함

* 영화 상세 정보에서 삭제버튼을 누르면 데이터가 삭제되고 영화 목록으로 가짐
  * 여기서 삭제 method가 POST일때만 삭제되도록 함
  * 삭제 버튼으로 삭제해야만 삭제가 됨

> 수정, 삭제하는 html을 작성하는게 가장 까다로웠는데, 수정은 new를 그대로 가져와 데이터만 넣어서 쉽게 만들었다. edit, update는 new, create과 똑같이 만들었다. 삭제할 때 method가 POST일때만 삭제되도록 해야 주소창에 임의로 /1/delete 이렇게 입력했을때 삭제되지 않는다. 





### 소감

이렇게 프로젝트를 만들어 봤는데, web시간에 html과 css를 배웠어서 그나마 쉽게 만들 수 있었고, bootstrap을 이용해서 디자인도 나름 할 수 있었다. 알고리즘하는거 뿐만 아니라 이렇게 웹페이지를 만드는 것도 정말 좋은 경험인 것 같다. 더욱 복잡한 페이지를 만들려면 얼마나 많은 양의 코드들이 있을지 모르겠다. 오류나는 부분이 정확히 안보여 만들 때 매우 까다로웠지만, 다 만들고 나니 뿌듯하다.