# DB 01

## Database

> 몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체
>
> 장점 : 데이터 중복 최소화, 데이터 무결성 (정확한 정보를 보장), 데이터 일관성, 데이터 독립성 (물리적 / 논리적), 데이터 표준화, 데이터 보안 유지

### RDB - 관계형 데이터베이스

> 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스

* 스키마 (schema) : 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것.
* 테이블 (table) : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합
* 열 (Column) : 각 열에는 고유한 데이터 형식이 지정됨
* 행 (row) : 실제 데이터가 저장되는 형태  (==레코드)
* 기본키 (Primary Key) : 각 행(레코드)의 고유 값, 반드시 설정해야 함



### RDBMS - 관계형 데이터베이스 관리 시스템 

>  Relational Database Management System - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
>
> 예시 - MySQL, SQLite, PostgreSQL, ORACLE, MS SQL

* SQLite : 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
  *  구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능



--------

## SQL (Structured Query Language)

> 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 프로그래밍 언어
>
> 데이터베이스 스키마 생성 및 수정, 자료의 검색 및 관리, 데이터베이스 객체 접근 조정 관리

| 분류                                                | 개념                                                         | 예시                         |
| --------------------------------------------------- | ------------------------------------------------------------ | ---------------------------- |
| DDL - 데이터 정의 언어 (Data Definition Language)   | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE DROP ALTER            |
| DML - 데이터 조작 언어 (Data Manipulation Language) | 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어        | INSERT SELECT UPDATE DELETE  |
| DCL - 데이터 제어 언어 (Data Control Language)      | 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어       | GRANT REVOKE COMMIT ROLLBACK |



### ■ 테이블 생성 및 삭제

* 데이터베이스 생성하기

```sqlite
$ sqlite3 tutorial.sqlite3
sqlite> .database
```

> . 은 sqlite 프로그램의 기능을 실행하는 것
>
> . 없으면 db에 명령하는 것

* csv 파일을 table로 만들기 : examples 테이블

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples 
sqlite> .tables
examples
```

* SELECT : SELECT 문은 특정 테이블의 레코드(행) 정보를 반환!

```sqlite
sqlite> SELECT * FROM examples;      
1,"길동","홍",600,"충청도",010-2424-1232
```

* (Optional) 터미널 view 변경하기

```sqlite
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------  
1   길동          홍          600  충청도      010-2424-1232
```



* CREATE - 테이블 생성 및 확인하기

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .table
classmates  examples
```

* 특정 테이블의 schema 조회 - 방금 전 생성한 classmates 테이블의 스키마

```sqlite
sqlite> .schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);
```

* DROP - 테이블 삭제

```sqlite
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```



#### DATA types

```sqlite
CREATE TABLE tableN(
id INTEGER,
name TEXT);
INSERT INTO tableN values('2', 10.1);
INSERT INTO tableN values('2', 10);
INSERT INTO tableN values('2b', 'TEST');

SELECT id, typeof(id), name, typeof(name) FROM tableN;
id,typeof(id),name,typeof(name)
2,integer,10.1,text
2,integer,10,text
2b,text,TEST,text
```

> 값을 읽고 유동적으로 데이터 타입을 바꿈





### ■ CRUD

#### 1. CREATE

* INSERT - `INSERT INTO 테이블이름 (칼럼1, 칼럼2, ...) VALUES (값1, 값2, ...);` 

  * 특정 테이블에 레코드(행)를 삽입(생성)!

  ```sqlite
  sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동',23);
  sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울');
  sqlite> SELECT * FROM classmates;
  name  age  address
  ----  ---  -------
  홍길동   23
  홍길동   30   서울
  ```

  > 모든 열에 데이터가 있는 경우 column을 명시하지 않아도 됨!

  * rowid
    * SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK 옵션을 가진 rowid 컬럼을 정의
  * NULL
    * 주소가 꼭 필요한 정보라면 공백으로 비워두면 안된다. (NOT NULL 설정 필요)

* 다시 새로 만들기

  ```sqlite
  sqlite> DROP TABLE classmates;
  sqlite> CREATE TABLE classmates (
     ...> id INTEGER PRIMARY KEY,
     ...> name TEXT NOT NULL,
     ...> age INT NOT NULL,
     ...> address TEXT NOT NULL
     ...> );
  sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울');
  Error: table classmates has 4 columns but 3 values were supplied
  ```

  > 스키마에 id를 직접 작성했기 때문에 입력할 column들을 명시하지 않으면 자동으로 입력되지 않음

  * (1) id를 포함한 모든 value를 작성

    ```sqlite
    sqlite> INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
    ```

  * (2) 각 value에 맞는 column들을 명시적으로 작성

    ```sqlite
    sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
    ```

  ```sqlite
  sqlite> SELECT * FROM classmates;
  id  name  age  address
  --  ----  ---  -------
  1   홍길동   30   서울
  2   홍길동   30   서울
  ```

* INSERT 하기

  ```sqlite
  sqlite> CREATE TABLE classmates (
     ...> name TEXT NOT NULL,
     ...> age INT NOT NULL,
     ...> address TEXT NOT NULL
     ...> );
  sqlite> INSERT INTO classmates VALUES
     ...> ('홍길동', 30, '서울'),
     ...> ('김철수', 30, '대전'),
     ...> ('이싸피', 26, '광주'),
     ...> ('박삼성', 29, '구미'),
     ...> ('최전자', 28, '부산');
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   30   서울
  2      김철수   30   대전
  3      이싸피   26   광주
  4      박삼성   29   구미
  5      최전자   28   부산
  ```

  

#### 2. READ

* SELECT - `SELECT 컬럼1, 컬럼2, ... FROM 테이블이름;` 

  * 테이블에서 데이터를 조회, SQLite에서 가장 복잡한 문이며 다양한 절(clause)와 함께 사용
    * ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY …

  * Limit : 쿼리에서 반환되는 행 수를 제한, 특정 행부터 시작해서 조회하기 위해 OFFSET 키워드와 함께 사용하기도 함
  * Where : 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
  * SELECT DISTINCT : 조회 결과에서 중복 행을 제거, DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  ```sqlite
  sqlite> SELECT rowid, name FROM classmates;
  rowid  name
  -----  ----
  1      홍길동
  2      김철수
  3      이싸피
  4      박삼성
  5      최전자
  ```

  ```sqlite
  sqlite> SELECT rowid, name FROM classmates LIMIT 1;   
  rowid  name
  -----  ----
  1      홍길동
  sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
  rowid  name
  -----  ----
  3      이싸피
  ```

  > LIMIT 1 : 하나만 조회
  >
  > LIMIT 1 OFFSET 2 : 세번째에 있는 하나만 조회

  ```sqlite
  sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
  rowid  name
  -----  ----
  1      홍길동
  ```

  ```sqlite
  sqlite> SELECT DISTINCT age FROM classmates;
  age
  ---
  30
  26
  29
  28
  ```

  

#### 3. DELETE

* DELETE - `DELETE FROM 테이블이름 WHERE 조건;`

  * 테이블에서 행을 제거
  * 중복 불가능한(UNIQUE) 값인 rowid를 기준으로 삭제하자!

  ```sqlite
  sqlite> DELETE FROM classmates WHERE rowid=5; 
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   30   서울
  2      김철수   30   대전
  3      이싸피   26   광주
  4      박삼성   29   구미
  ```

  > 5가 없을때 지워도 아무일도 없음. 데이터를 확인하고 지우는게 아니라 바로 지워서 

  ```sqlite
  sqlite> INSERT INTO classmates VALUES ('최전자',28,'부산');     
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   30   서울
  2      김철수   30   대전
  3      이싸피   26   광주
  4      박삼성   29   구미
  5      최전자   28   부산
  ```

  > SQLite는 기본적으로 id를 재사용

* AUTOINCREMENT - SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

  ```
  CREATE TABLE 테이블이름 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ...
  );
  ```

  > 테이블을 생성하는 단계에서 AUTOINCREMENT를 통해 설정가능



#### 4. UPDATE

* UPDATE - `UPDATE 테이블이름 SET 칼럼1=값1, ... WHERE 조건;`

  * 기존 행의 데이터를 수정 
  * SET clause에서 테이블의 각 열에 대해 새로운 값을 설정
  * 중복 불가능한(UNIQUE) 값인 rowid를 기준으로 수정하자!

  ```sqlite
  sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
  sqlite> SELECT rowid, * FROM classmates;
  rowid  name  age  address
  -----  ----  ---  -------
  1      홍길동   30   서울
  2      김철수   30   대전
  3      이싸피   26   광주
  4      박삼성   29   구미
  5      홍길동   28   제주도
  ```

  

#### ◇ CRUD 정리하기

|      | 구문   | 예시                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2); |
| R    | SELECT | SELECT * FROM 테이블이름 WHERE 조건;                         |
| U    | UPDATE | UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;       |
| D    | DELETE | DELETE FROM 테이블이름 WHERE 조건;                           |



### ■ WHERE

```sqlite
sqlite> CREATE TABLE users (
sqlite> first_name TEXT NOT NULL,
sqlite> last_name TEXT NOT NULL,
sqlite> age INTEGER NOT NULL,
sqlite> country TEXT NOT NULL,
sqlite> phone TEXT NOT NULL,
sqlite> balance INTEGER NOT NULL
sqlite> );

sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables
```

> 테이블 만든 후 csv파일에서 데이터 가져오기

```sqlite
sqlite> SELECT * FROM users WHERE age >= 30;
sqlite> SELECT * FROM users WHERE age >= 30 AND last_name='김';
```



### ■ Sqlite Aggregate Functions

* COUNT - 그룹의 항목 수를 가져옴
* AVG - 값 집합의 평균 값을 계산
* MAX - 그룹에 있는 모든 값의 최대값을 가져옴 
* MIN - 그룹에 있는 모든 값의 최소값을 가져옴 
* SUM - 모든 값의 합을 계산

> AVG, MAX, MIN, SUM - 기본적으로 해당 컬럼이 숫자(INTEGER)일 때만 사용 가능

```sqlite
sqlite> SELECT COUNT(*) FROM users;
COUNT(*)
1000
```

```sqlite
sqlite> SELECT AVG(age) FROM users WHERE age>=30;
AVG(age)
35.1763285024155
```

```sqlite
sqlite> SELECT first_name, MAX(balance) FROM users;
first_name,MAX(balance)
"순옥",1000000
```

```sqlite
sqlite> SELECT AVG(balance) FROM users WHERE age>=30;
AVG(balance)
153541.425120773
```



### ■ LIKE

* `SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';`
* 패턴 일치를 기반으로 데이터를 조회하는 방법
* sqlite는 패턴 구성을 위한 2개의 wildcards를 제공
  * % (percent sign) - 0개 이상의 문자. 이 자리에 문자열이 있을 수도, 없을 수도 있다.
  * _ (underscore) - 임의의 단일 문자. 반드시 이 자리에 한 개의 문자가 존재해야 한다.
    * `2_%_% / 2__%` : 2로 시작하고 적어도 3자리인 값

```sqlite
sqlite> SELECT * FROM users WHERE phone LIKE '2_';
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';
sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%'; 
```



### ■ ORDER BY

* `SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2 ASC;`
* 조회 결과 집합을 정렬
* SELECT 문에 추가하여 사용
* 정렬 순서를 위한 2개의 keyword 제공 : ASC – 오름차순 (default), DESC - 내림차순

```sqlite
sqlite> SELECT * FROM users ORDER BY age ASC, last_name DESC LIMIT 10;
sqlite> SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```



### ■ GROUP BY

* `SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;`
* 행 집합에서 요약 행 집합을 만듦
* SELECT 문의 optional 절
* 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
* 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함

```sqlite
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

> AS 를 활용해서 COUNT에 해당하는 컬럼 명을 바꿔서 조회할 수 있음



### ■ ALTER TABLE

* 3가지 기능 : (1) table 이름 변경 (2) 테이블에 새로운 column 추가 (3) [참고] column 이름 수정
* `ALTER TABLE 기존테이블이름 RENAME TO 새로운테이블이름;`
* `ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입설정;`

```sqlite
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;   
Error: Cannot add a NOT NULL column with default value NULL 
```

> 테이블에있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다. 
>
> 그렇기 때문에 NOT NULL 형태의 컬럼은 추가가 불가능!
>
> => 1. NOT NULL 설정 없이 추가하기 2. 기본 값(DEFAULT) 설정하기

```sqlite
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT;
sqlite> INSERT INTO news VALUES ('제목', '내용', datetime('now'));
sqlite> SELECT * FROM news;
title  content  created_at
-----  -------  -------------------
1번제목   1번내용
제목     내용       2021-09-14 05:19:55
```

```sqlite
sqlite> ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';
sqlite> SELECT * FROM news;
title  content  created_at           subtitle
-----  -------  -------------------  --------
1번제목   1번내용                          소제목
제목     내용       2021-09-14 05:19:55  소제목
```





---------

## SQL & ORM

> Django Project Setting - 가상환경 적용
>
> ```
> $ pip install –r requirements.txt
> $ python manage.py migrate
> $ python manage.py sqlmigrate users 0001
> $ sqlite3 db.sqlite3
> ```

```sqlite
sqlite> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            users_user
auth_user_user_permissions
```

* csv 파일을 데이터 베이스에 적용하기

  ```sqlite
  sqlite> .mode csv
  sqlite> .import users.csv users_user
  sqlite> SELECT * FROM users_user;
  ```


> json : `$ python manage.py loaddata users/users.json`

* 스키마 확인

  ```sqlite
  sqlite> .schema users_user
  CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
  ```

* .headers on

  ```sqlite
  sqlite> .headers on
  sqlite> SELECT * FROM users_user;
  id,first_name,last_name,age,country,phone,balance
  ...
  ```

  

### ■ CRUD

#### 1. READ - 모든 user 레코드 조회

* ORM - `USER.objects.all()`
* SQL - `SELECT * FROM users_user;`



#### 2. CREATE

* ORM 

  ```shell
  User.objects.create(
  	first_name='길동',
  	last_name='홍',
  	age=100,
  	country='제주도',
  	phone='010-1234-5678',
  	balance=10000
  )
  ```

* SQL

  ```sqlite
  sqlite> INSERT INTO users_user VALUES (102, '길동', '김', 100, '경상북도', '010-1234-1234', 100);
  sqlite> SELECT * FROM users_user LIMIT 2 OFFSET 100;
  id,first_name,last_name,age,country,phone,balance
  102,"길동","김",100,"경상북도",010-1234-1234,100
  ```

  

#### 3. READ - 특정 user 레코드 조회

* ORM

  ```shell
  User.objects.get(pk=102)
  ```

* SQL

  ```sqlite
  SELECT * FROM users_user WHERE id=102;
  ```
  
  

#### 4. UPDATE
* ORM

  ```shell
  user = User.objects.get(pk=102)
  user.last_name = '김'
  user.save()
  user.last_name
  ```

* SQL

  ```sqlite
  UPDATE users_user SET first_name='철수' WHERE id=102;
  SELECT * FROM users_user WHERE id=102;
  ```
  
  


#### 5. DELETE

* ORM

  ```shell
  User.objects.get(pk=102).delete()
  ```

* SQL

  ```sqlite
  DELETE FROM users_user WHERE id=102;
  SELECT * FROM users_user WHERE id=102;
  ```
  
  

### ■ SQL & ORM 활용하기

* 전체 유저의 수 조회 (ORM/SQL)

  ```python
  User.objects.count()
  ```

  ```sqlite
  SELECT COUNT(*) FROM users_user;
  ```

* #### 조건에 따른 쿼리문

* 특정조건으로 데이터를 조회 

  > 나이가 30살인 사람들의 이름을 조회 (ORM/SQL)

  ```python
  User.objects.filter(age=30).values('first_name')
  ```

  ```sqlite
  SELECT first_name FROM users_user WHERE age=30;
  ```

  * 쿼리문 확인하기 (ORM)

    ```python
    In [6]: print(User.objects.filter(age=30).values('first_name').query)
    SELECT "users_user"."first_name" FROM "users_user" WHERE "users_user"."age" = 30
    ```

* 대/소 관계 비교 조건 - `__gte, __gt, __lte, __lt` : 이상, 초과, 이하, 미만 (greater than, lighter than)

  > 나이가 30살 이상 / 20살 이하인 사람의 인원 수  (ORM)

  ```python
  User.objects.filter(age__gte=30).count()
  User.objects.filter(age__lte=20).count()
  ```

* AND

  > 나이가 30살이면서 성이 김씨인 사람의 인원 수  (ORM)

  ```python
  User.objects.filter(age=30, last_name='김').count()
  ```

* OR

  > 나이가 30살이거나 성이 김씨인 사람의 인원 수  (ORM)
  >
  > [참고] OR 을 활용하고 싶다면, Q object 를 활용해야 함
  >
  > ‘|’(OR) 및 ‘&’(AND)와 같은 연산자를 사용하여 조건을 정의 및 재사용

  ```python
  from django.db.models import Q
  User.objects.filter(Q(age=30) | Q(last_name='김'))
  ```

* LIKE

  > 지역번호가 02인 사람의 인원 수 (ORM/SQL)

  ```python
  User.objects.filter(phone__startswith='02-').count()
  User.objects.filter(first_name__endswith='수')
  User.objects.filter(phone__contains='123', age__lt=30).values()
  ```

  ```sqlite
  SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
  ```

  * 특정 컬럼 데이터만 조회하기

  > 주소가 강원도이면서 성이 황씨인 사람의 이름 (ORM)

  ```python
  User.objects.filter(country='강원도', last_name='황').values('first_name')
  ```

* 정렬, LIMIT, OFFSET

  > 나이가 많은 사람순으로 10명만 조회 (ORM)

  ```python
  User.objects.order_by('-age')[:10]
  ```

  > 잔액이 적은 사람순으로 10명만 조회 (ORM)

  ```python
  User.objects.order_by('balance')[:10]
  ```

  > 잔액이 적고, 나이가 많은순으로 10명만 조회 (ORM/SQL)

  ```python
  User.objects.order_by('balance', '-age')[:10]
  ```

  ```sqlite
  SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
  ```

  > 성, 이름 내림차순으로 5번째 있는 유저 정보 조회

  ```python
  User.objects.order_by('-last_name', '-first_name')[4]
  ```

  ```sqlite
  SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
  ```

* DISTINCT (ORM)

  ```
  User.objects.filter(phone__startswith='010').values('country').distinct()
  ```

  





-----------

## Django Aggregation

### aggregate()

> ‘무언가를 종합, 집합, 합계' 등의 사전적 의미
>
> 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용

* 성이 김씨인 유저들의 평균 나이 (ORM)

  ```python
  from django.db.models import Avg
  User.objects.filter(last_name='김').aggregate(Avg('age'))
  ```

* 지역이 강원도인 유저들의 평균 계좌 잔고 (ORM)

  ```python
  from django.db.models import Avg
  User.objects.filter(country='강원도').aggregate(Avg('balance'))
  ```

* 계좌 잔고의 총 합 (ORM)

  ```python
  from django.db.models import Sum
  User.objects.aggregate(Sum('balance'))
  ```

* 경상북도에 사는 사람 중 가장 많은 balance의 액수

  ```
  User.objects.filter(country='경상북도').aggregate(Max('balance'))
  ```

  

### annotate()

> ‘주석을 달다’라는 사전적 의미. 마치 컬럼 하나를 추가하는 것과 같음
>
> 특정 조건으로 계산된 값을 가진 컬럼를 하나 만들고 추가하는 개념
>
> annotate()에 대한 각 인자는 반환되는 QuerySet의 각 객체에 추가될 주석임

* 지역별 인원수 (ORM/SQL)

  * Annotate는 새로운 컬럼(주석)을 만들어 냄 (원본 테이블이 변하는 것이 아님)

  ```python
  from django.db.models import Count
  
  # 1
  User.objects.values('country').annotate(Count('country'))
  # <QuerySet [{'country': '강원도', 'country__count': 14}, ... 
  
  # 2
  User.objects.values('country').annotate(num_countries=Count('country'))
  #<QuerySet [{'country': '강원도', 'num_countries': 14}, ... 
  
  # 3
  print(User.objects.values('country').annotate(Count('country')).query)
  # SELECT "users_user"."country", COUNT("users_user"."country") AS "country__count" FROM "users_user" GROUP BY "users_user"."country"
  
  # 4
  User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
  # <QuerySet [{'country': '강원도', 'country__count': 14, 'avg_balance': 157895.0}, ... 
  ```

  ```sqlite
  sqlite> SELECT country, COUNT(country) FROM users_user GROUP BY country;
  country,COUNT(country)
  "강원도",14
  "경기도",9
  "경상남도",9
  "경상북도",16
  "전라남도",10
  "전라북도",11
  "제주도",1
  "제주특별자치도",9
  "충청남도",9
  "충청북도",14
  ```

  







































