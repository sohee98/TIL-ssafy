# branch

> https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html

```bash
$ touch README.md .gitignore
$ git init
```

> master 이름의 브랜치 자동 생성

```bash
$ git add .
$ git commit -m 'first commit'
```

> root-commit => 있어야 브랜치 생성 가능



1. branch는 단순한 포인터(화살표)다.

2. HEAD 는 단순한 포인터다. (포인터의 포인터인 경우가 많다.)

   > commit 6ef6a835454aaa1dee52a005a0eead13f8e6de98 (HEAD -> master)

3. HEAD는 현재 내가 작업중인 커밋을 의미한다.

4. Head가 master에 있다. == 현재 master에서 작업중이다.



```bash
$ git commit -m '2 commit'
$ git log --oneline
12dbbfe (HEAD -> master) 2 commit
6ef6a83 first commit
```

```bash
$ git commit -m '3 commit'
$ git log --oneline
fc5cadf (HEAD -> master) 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> head -> master 현재 commit한 곳으로 이동



#### branch 만들기 - b1

```bash
$ git branch b1
$ git log --oneline
fc5cadf (HEAD -> master, b1) 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> 마지막으로 commit한 위치에서 branch가 생성 됨 (3 commit)

```bash
$ git switch b1
Switched to branch 'b1'

sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (b1)
$ git log --oneline
fc5cadf (HEAD -> b1, master) 3 commit
```

> head를 branch로 이동  (오른쪽 괄호 == 브랜치)



* branch에서 commit

```bash
$ git commit -m '4 commit'
$ git log --oneline
667cc04 (HEAD -> b1) 4 commit
fc5cadf (master) 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> b1에서 4 commit 발생



* 새로운 파일 생성 후 branch에서 commit

```bash
$ touch secret.txt
```

> 커밋 안하면 git은 모르는 파일
>
> `$ git status` => Untracked files : 

```bash
sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (b1)
$ git commit -m '5 commit'
```

```bash
$ git log --oneline
49a2925 (HEAD -> b1) 5 commit
667cc04 4 commit
fc5cadf (master) 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> b1에서 commt =>` $ git switch master` 하면 secret.txt 파일 안보임



```bash
$ git switch master
$ git log --oneline
fc5cadf (HEAD -> master) 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> master에서는 master가 commit한 부분까지만 보임



#### branch 합치기

* 더 큰 단위인 master에서 작업
* Fast-forward 방식

```bash
$ git switch master
$ git merge b1
Updating fc5cadf..49a2925
Fast-forward
 README.md  | 1 +
 secret.txt | 0
 2 files changed, 1 insertion(+)
 create mode 100644 secret.txt 
```

```bash
$ git log --oneline
49a2925 (HEAD -> master, b1) 5 commit
667cc04 4 commit
fc5cadf 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> master가 5 commit으로 이동



#### 새로운 branch - b2

```bash
$ git branch b2
$ git branch 		#목록 보기
  b1
  b2
* master
```

```bash
$ git switch b2
$ touch b2.txt
$ git add .
$ git commit -m '6 commit'
$ git add .
$ git commit -m '7 commit'
```

```bash
$ git log --oneline
427c3a0 (HEAD -> b2) 7 commit
70b94bd 6 commit
49a2925 (master, b1) 5 commit
667cc04 4 commit
fc5cadf 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> branch b2에서 7 commit 작업



* master에서 작업

```bash
$ git switch master
# README.md 수정
$ git add .
$ git commit -m '8 commit'

$ touch master.txt	# master.txt 수정
$ git add .
$ git commit -m '9 commit'
```

```bash
sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline
7de2f81 (HEAD -> master) 9 commit
25e68a8 8 commit
49a2925 (b1) 5 commit
667cc04 4 commit
fc5cadf 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> master에서 9 commit 작업



#### Auto Merge

* master와 b2 합치기

```bash
$ git switch master

sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master)
$ git merge b2
Merge made by the 'recursive' strategy.
 b2.txt | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 b2.txt
```

```bash
sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline
19de522 (HEAD -> master) Merge branch 'b2'
7de2f81 9 commit
25e68a8 8 commit
427c3a0 (b2) 7 commit
70b94bd 6 commit
49a2925 (b1) 5 commit
667cc04 4 commit
fc5cadf 3 commit
12dbbfe 2 commit
6ef6a83 first commit
```

> 자동으로 작성된 commit : `Merge branch 'b2'`



```bash
$ git log --oneline --graph
*   19de522 (HEAD -> master) Merge branch 'b2'
|\
| * 427c3a0 (b2) 7 commit
| * 70b94bd 6 commit
* | 7de2f81 9 commit
* | 25e68a8 8 commit
|/
* 49a2925 (b1) 5 commit
* 667cc04 4 commit
* fc5cadf 3 commit
* 12dbbfe 2 commit
* 6ef6a83 first commit
```



#### 새로운 branch - b3

```bash
$ git switch -c b3	
```

> branch 생성하면서 이동까지 함

```bash
$ touch b3.txt
$ git add .
$ git commit -m '11 commit'
# secret.txt 수정
$ git add .
$ git commit -m '12 commit'
```



* master에서 작업

```bash
$ git switch master
# mater.txt 수정
$ git add .
$ git commit -m '13 commit'
# secret.txt 수정
$ git add .
$ git commit -m '14 commit'
```



#### Manual merge (conflict) 

* 둘 다 수정한 secret.txt 에서 충돌

```bash
sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master)
$ git merge b3
Auto-merging secret.txt
CONFLICT (content): Merge conflict in secret.txt
Automatic merge failed; fix conflicts and then commit the result.
```

```bash
sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master|MERGING)
$ 
```

> (master|MERGING) -> 아직 병합 중

```bash
# secret.txt에서 수정 후 저장
$ git add .
$ git commit -m '15 - conflict merge'

sohee@DESKTOP-OU8BKJJ MINGW64 ~/Desktop/git_branch (master)
$ 
```

```bash
$ git log --oneline --graph
*   0a52854 (HEAD -> master) 15 - conflict merge
|\
| * 88aedd6 (b3) 12 commit
| * 451bc92 11 commit
* | 2db57da 14 commit
* | cd74fbc 13 commit
|/
*   19de522 Merge branch 'b2'
|\
| * 427c3a0 (b2) 7 commit
| * 70b94bd 6 commit
* | 7de2f81 9 commit
* | 25e68a8 8 commit
|/
* 49a2925 (b1) 5 commit
* 667cc04 4 commit
* fc5cadf 3 commit
* 12dbbfe 2 commit
* 6ef6a83 first commit
```

* merge를 완료한 branch는 다시 보지 않으므로 삭제 





# Push

* gitlab에서 repository 생성
  * README 처음 자동 생성

* dev-a, dev-b 따로 각 폴더에서 작업

* 브랜치 따로 업로드 

  ```bash
  $ git push origin dev-a
  ```

  ```bash
  $ git push origin dev-b
  ```




* merge 방법 - gitlab에서
  * 프로젝트 개요 탭 > create merge request 버튼 - dev-b 병합
  * Merge Request 탭 > New merge request 버튼 - dev-a 병합
    * source branch : dev-a
    * target branch : master
  



* 병합 후 파일 받아오기 (a, b 각각 입력)

  ```bash
  $ git switch master
  $ git pull origin master
  ```



* 브랜치 지우기 

  ```bash
  $ git branch -d dev-a
  $ git branch -d dev-b
  ```

  ```bash
  $ git branch
  ```

  > 목록에서 사라짐



* 새로운 브랜치 

  ```bash
  $ git switch -c 'dev2-a'
  # 작업 -> commit
  $ git push origin dev2-a
  ```

  ```bash
  $ git switch -c 'dev2-b'
  # 작업 -> commit
  $ git push origin dev2-b
  ```

* merge하면 충돌이 일어남 
  * dev2-b merge
  * dev2-a merge할 때 충돌 -> 수정 







