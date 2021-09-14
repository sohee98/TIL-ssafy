-- 1. CREATE
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

-- 2. READ
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
sqlite> SELECT DISTINCT age FROM classmates; 

-- 3. DELETE
sqlite> DELETE FROM classmates WHERE rowid=5; 

-- 4. UPDATE
sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;






