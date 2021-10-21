### 1. M:N True or False 

.각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고, 틀렸다면 그 이유도 함께 작성하시오. 

1) Django에서1:N 관계는 ForeignKeyField를 사용하고, M:N 관계는 ManyToManyField를 사용한다.
   * F (ForeignKey, ManyToManyField 사용)
2) ManyToManyField를 설정하고 만들어지는 테이블 이름은 `“앱이름_클래스이름_지정한 필드이름”`의 형태로 만들어진다.
   * T 
3) ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.
   * F (첫번째 인자는 필수인데, related_name은 역참조할때 사용할 이름으로 기본값=`클래스이름_set`이 설정되어 있기에 필수는 아니다.)



### 2. Like in templates

(a) user

(b) article.like_users.all



### 3. Follow in views

(a) user_pk

(b) followers

(c) filter

(d) add

(e) remove



### 4. User AttributeError 

다음과 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하시오

* 프로젝트 중간에 User모델을 커스텀 유저 모델로 변경하였기 때문이다.

* 방법:

  * db.sqlite3 파일 삭제
  * migrations 파일 모두 삭제

* ```
  $ python manage.py makemigrations
  $ python manage.py migrate
  ```

  데이터베이스를 초기화 후 마이그레이션을 진행한다.



### 5. related_name

아래의 경우 ForeignKey 혹은 ManyToManyField에 related_name을 필수적으로 작성해야 한다. 그 이유를 설명하시오. 

* like_users 필드 생성 시 자동으로 역참조는 .article_set 매니저를 생성하는데 이전 user 필드에서 이미 해당 매니저 이름을 사용중이기 때문에 오류가 발생한다.
* 그래서 둘중 하나에 related_name을 추가하여 이름을 바꿔줘야 한다. 



### 6. follow templates

person 변수에는 view함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때 빈칸 a, b, c, d, e에 들어갈 알맞은 코드를 각각 작성하시오.

(a) person.followings.all

(b) person.followers.all

(c) user

(d) person

(e) person.pk









